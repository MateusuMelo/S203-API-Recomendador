import pandas as pd
import pytest
from unittest.mock import patch, MagicMock
from server.recommender.components.recommender import (
    get_user_ratings,
    get_top_movies,
    get_movie_list,
    get_user_unrated_movies,
    get_similar_movies,
    get_final_recommendations,
)

@pytest.fixture
def sample_ratings_data():
    return pd.DataFrame({'rating': [5, 4, 3], 'movie_id': [101, 102, 103]})

@pytest.fixture
def sample_movies_data():
    return pd.DataFrame({'movie_id': [101, 102, 103], 'genre': ['Action', 'Comedy', 'Drama']})

@pytest.fixture
def sample_user_id():
    return 1

def test_get_user_ratings(sample_ratings_data):
    with patch('server.recommender.components.database.Database.query', return_value=[(5, 101), (4, 102), (3, 103)]):
        ratings = get_user_ratings(sample_user_id)
        assert ratings.equals(sample_ratings_data)

def test_get_final_recommendations(sample_movies_data):
    similar_movies = pd.DataFrame({'movie_id': [101, 102], 'similarity_coefficient': [0.5, 0.6]})

    final_list = get_final_recommendations(similar_movies)
    assert final_list is not None

def test_get_top_movies(sample_ratings_data):
    with patch('server.recommender.components.database.Database.query', return_value=[(5, 101), (4, 102), (3, 103)]):
        top_movies = get_top_movies()
        expected_json = sample_ratings_data[['movie_id', 'rating']].astype(float).to_json(orient="table", index=False)
        assert top_movies == expected_json

def test_get_movie_list(sample_movies_data):
    with patch('server.recommender.components.database.Database.query', return_value=[(101, 'Action'), (102, 'Comedy'), (103, 'Drama')]):
        movies = get_movie_list()
        assert movies.equals(sample_movies_data)

def test_get_user_unrated_movies(sample_ratings_data, sample_movies_data):
    user_ratings_mock = MagicMock(return_value=sample_ratings_data)
    movie_list_mock = MagicMock(return_value=sample_movies_data)

    with patch('server.recommender.components.recommender.get_user_ratings', user_ratings_mock), \
         patch('server.recommender.components.recommender.get_movie_list', movie_list_mock):
        unrated_movies = get_user_unrated_movies(sample_user_id, sample_ratings_data, sample_movies_data)
        assert len(unrated_movies) == 0

def test_get_similar_movies(sample_movies_data):
    user_movies = pd.DataFrame({'movie_id': [101], 'genre': [['Action']]})

    with patch('server.recommender.components.recommender.get_similar', return_value=pd.DataFrame({'movie_id': [102], 'similarity_coefficient': [0.5]})):
        similar_movies = get_similar_movies(user_movies, sample_movies_data)
        assert len(similar_movies) == 1


