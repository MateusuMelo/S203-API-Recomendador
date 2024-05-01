import pandas as pd
import json
from .database import Database
from sklearn.metrics import jaccard_score


def get_recommendation(user_id):
    args = f"SELECT rating, movie_id FROM recommend_myrating WHERE user_id = {user_id}"  # Lista de avaliações do usuario
    results = Database().query(args)
    rating_list = pd.DataFrame(results, columns=["rating", "movie_id"])

    if not results:  # Caso o usuario não exista retorna os filmes e as medias de avaliação
        best_movies = f"SELECT rating, movie_id FROM recommend_myrating ORDER BY rating DESC"  # filtrando todos as avaliações, ordenando da maior nota para a menor
        results = Database().query(best_movies)

        rating_list = pd.DataFrame(results, columns=["rating", "movie_id"])

        # Calculando a média da coluna 'outra_coluna' para cada 'movie_id' e removendo os valores duplicados by gpt
        rating_list = rating_list.groupby('movie_id').agg({'rating': 'mean'}).reset_index()

        rating_list = rating_list[['movie_id', 'rating']].sort_values(by=['rating'],
                                                                      ascending=False)  # ordenando pela nota

        rating_list = rating_list[['movie_id', 'rating']].to_json(index=False, orient="table")
        return rating_list

    args = f"SELECT id, genre FROM recommend_movie"  # Lista de avaliações do usuario
    results = Database().query(args)
    movie_list = pd.DataFrame(results, columns=["movie_id", "genre"])
    print(movie_list)
    movie_list['genre'] = movie_list['genre'].str.split(
        ',')  # transformando genre em uma lista de strings. Estava uma unica string

    unique_genres = set()  # obtendo uma lista de todos os generos
    for genres in movie_list['genre']:
        unique_genres.update(genres)

    genre_to_number = {genre: i for i, genre in enumerate(unique_genres)}  # definindo genero por numero inteiro
    movie_list['genre_id'] = movie_list['genre'].map(
        lambda x: [genre_to_number[genre] for genre in x])  # adicionando o mapa na coluna de genre_id

    movie_list['genre_id'] = movie_list['genre_id'].apply(lambda x: x + [-1] * (
            3 - len(x)))  # padronizando numero de generos para 3, e adicionando -1 nos generos faltantes

    # Selecionar os filmes que não foram avaliados pelo usuario
    merged = pd.merge(movie_list, rating_list, how='outer', indicator=True)
    user_movies = merged[merged['_merge'] == 'both'].drop('_merge', axis=1)
    user_movies = user_movies.drop(user_movies[user_movies.rating <= 3].index)

    final_list = pd.DataFrame(columns=('index', 'movie_id', 'similarity_coefficient'))
    for movie_id_user in user_movies['movie_id']:
        similar_movies = json.loads(get_similar(movie_id_user))['data']
        for data in similar_movies:
            final_list.loc[len(final_list.index)] = data

    final_list = final_list.groupby('movie_id').agg({'similarity_coefficient': 'mean'}).reset_index()
    final_list = final_list.sort_values(by=['similarity_coefficient'], ascending=False)  # ordenando pela nota
    final_list = final_list[['movie_id', 'similarity_coefficient']].to_json(index=None, orient="table")
    return final_list

def get_similar(id_movie):
    args = f"SELECT id, genre FROM recommend_movie"  # Lista de de filmes
    results = Database().query(args)
    movie_list = pd.DataFrame(results, columns=["movie_id", "genre"])  # lista de filmes em um DF

    # transformando genre em uma lista de strings. Estava uma unica string
    movie_list['genre'] = movie_list['genre'].str.split(
        ',')

    # obtendo uma lista de todos os generos unicos
    unique_genres = set()
    for genres in movie_list['genre']:
        unique_genres.update(genres)

    # definindo cada genero por numero inteiro
    genre_to_number = {genre: i for i, genre in enumerate(unique_genres)}

    # adicionando o mapa na coluna de genre_id
    movie_list['genre_id'] = movie_list['genre'].map(
        lambda x: [genre_to_number[genre] for genre in x])

    # padronizando genr_id.shape (1,3), e adicionando -1 nos generos faltantes  ex: gen [1,2] agora [1,2,-1]
    movie_list['genre_id'] = movie_list['genre_id'].apply(lambda x: x + [-1] * (
            3 - len(x)))

    movie_request = movie_list.loc[movie_list['movie_id'] == int(id_movie)]  # Selecionando filme requisitado.

    movie_list = movie_list[
        movie_list['movie_id'] != int(id_movie)]  # removendo filme requisitado da lista de todos os filmes.

    # Aplicando metrica de semelhança Jaccard para cada filme com relação ao filme selecionado
    for index, row in movie_list.iterrows():
        y_true = row['genre_id']
        y_pred = movie_request.iloc[0]['genre_id']
        movie_list.at[index, 'similarity_coefficient'] = jaccard_score(y_true, y_pred, average='weighted')

    final_list = movie_list[['movie_id', 'similarity_coefficient']].sort_values(by=['similarity_coefficient'],
                                                                                ascending=False)  # ordenando pela nota

    final_list = final_list[['movie_id', 'similarity_coefficient']].to_json(index=None, orient="table")

    return final_list
