import pandas as pd
import json
from .database import Database
from sklearn.metrics import jaccard_score

def get_recommendation(user_id):
    rating_list = get_user_ratings(user_id)
    if not rating_list:
        return get_top_movies()

    movie_list = get_movie_list()
    user_movies = get_user_unrated_movies(user_id, rating_list, movie_list)

    similar_movies = get_similar_movies(user_movies, movie_list)

    final_list = get_final_recommendations(similar_movies)

    return final_list

def get_user_ratings(user_id):
    args = f"SELECT rating, movie_id FROM recommend_myrating WHERE user_id = {user_id}"
    results = Database().query(args)
    rating_list = pd.DataFrame(results, columns=["rating", "movie_id"])
    return rating_list

def get_top_movies():
    best_movies_query = "SELECT rating, movie_id FROM recommend_myrating ORDER BY rating DESC"
    results = Database().query(best_movies_query)
    rating_list = pd.DataFrame(results, columns=["rating", "movie_id"])

    rating_list = rating_list.groupby('movie_id').agg({'rating': 'mean'}).reset_index()
    rating_list = rating_list.sort_values(by='rating', ascending=False)
    rating_list = rating_list[['movie_id', 'rating']].to_json(index=False, orient="table")
    return rating_list

def get_movie_list():
    args = "SELECT id, genre FROM recommend_movie"
    results = Database().query(args)
    movie_list = pd.DataFrame(results, columns=["movie_id", "genre"])
    movie_list['genre'] = movie_list['genre'].str.split(',')
    return movie_list

def get_user_unrated_movies(user_id, rating_list, movie_list):
    merged = pd.merge(movie_list, rating_list, how='outer', indicator=True)
    user_movies = merged[merged['_merge'] == 'both'].drop('_merge', axis=1)
    user_movies = user_movies[user_movies.rating > 3]
    return user_movies

def get_similar_movies(user_movies, movie_list):
    similar_movies_list = []

    for movie_id_user in user_movies['movie_id']:
        similar_movies = get_similar(movie_id_user, movie_list)
        similar_movies_list.extend(similar_movies)

    return pd.DataFrame(similar_movies_list, columns=['movie_id', 'similarity_coefficient'])

def get_similar(movie_id_user, movie_list):
    movie_request = movie_list.loc[movie_list['movie_id'] == movie_id_user].copy()
    movie_list = movie_list[movie_list['movie_id'] != movie_id_user]

    movie_request_genre = movie_request.iloc[0]['genre']
    movie_list['similarity_coefficient'] = movie_list['genre'].apply(lambda x: jaccard_score(movie_request_genre, x))

    return movie_list[['movie_id', 'similarity_coefficient']]

def get_final_recommendations(similar_movies):
    final_list = similar_movies.groupby('movie_id').agg({'similarity_coefficient': 'mean'}).reset_index()
    final_list = final_list.sort_values(by='similarity_coefficient', ascending=False)
    final_list = final_list[['movie_id', 'similarity_coefficient']].to_json(index=False, orient="table")
    return final_list
