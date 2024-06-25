import pandas as pd
from .database import Database
from sklearn.metrics import jaccard_score

class Recommender:
    def __init__(self, db_file):
        self.db = Database(db_file)

    def get_recommendation(self, user_id):
        # Tentar obter os ratings do usuário `user_id`. Se ele 
        # ainda não avaliou nada, retornamos apenas os filmes
        # com melhor avaliação.
        rating_list = self.get_user_ratings(user_id)
        if not rating_list:
            return self.get_top_movies()

        movie_list = self.get_movie_list()
        user_movies = self.get_user_unrated_movies(rating_list, movie_list)

        similar_movies = self.get_similar_movies(user_movies, movie_list)
        final_list = self.get_final_recommendations(similar_movies)

        return final_list

    def get_user_ratings(self, user_id):
        stmt = "SELECT rating, movie_id FROM recommend_myrating WHERE user_id = ?"
        results = self.db.execute_query(stmt, user_id)
        rating_list = pd.DataFrame(results, columns=["rating", "movie_id"])

        return rating_list

    # Retorna os todos os filmes com as notas mais altas no banco
    def get_top_movies(self):
        best_movies_query = "SELECT rating, movie_id FROM recommend_myrating ORDER BY rating DESC"
        results = self.db.execute_query(best_movies_query)
        rating_list = pd.DataFrame(results, columns=["rating", "movie_id"])

        rating_list = rating_list.groupby('movie_id').agg({'rating': 'mean'}).reset_index().sort_values(by='rating', ascending=False)
        return rating_list[['movie_id', 'rating']].to_json(index=False, orient="table")

    # Retorna todos os pares `id` e `genre` correspondentes aos filmes no banco
    def get_movie_list(self):
        args = "SELECT id, genre FROM recommend_movie"
        results = self.db.execute_query(args)
        movie_list = pd.DataFrame(results, columns=["movie_id", "genre"])
        movie_list['genre'] = movie_list['genre'].str.split(',')

        return movie_list

    def get_user_unrated_movies(self, rating_list, movie_list):
        merged = pd.merge(movie_list, rating_list, how='outer', indicator=True)
        user_movies = merged[merged['_merge'] == 'both'].drop('_merge', axis=1)
        user_movies = user_movies[user_movies.rating > 3]

        return user_movies

    def get_similar_movies(self, user_movies, movie_list):
        similar_movies_list = []

        for movie_id_user in user_movies['movie_id']:
            similar_movies = self.get_similar(movie_id_user, movie_list)
            similar_movies_list.extend(similar_movies)

        return pd.DataFrame(similar_movies_list, columns=['movie_id', 'similarity_coefficient'])

    def get_similar(self, movie_id_user, movie_list):
        movie_request = movie_list.loc[movie_list['movie_id'] == movie_id_user].copy()
        movie_list = movie_list[movie_list['movie_id'] != movie_id_user]

        movie_request_genre = movie_request.iloc[0]['genre']
        movie_list['similarity_coefficient'] = movie_list['genre'].apply(lambda x: jaccard_score(movie_request_genre, x))

        return movie_list[['movie_id', 'similarity_coefficient']]

    def get_final_recommendations(self, similar_movies):
        final_list = similar_movies.groupby('movie_id').agg({'similarity_coefficient': 'mean'}).reset_index()
        final_list = final_list.sort_values(by='similarity_coefficient', ascending=False)
        final_list = final_list[['movie_id', 'similarity_coefficient']].to_json(index=False, orient="table")

        return final_list
