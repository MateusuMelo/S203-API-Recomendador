import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from server.recommender.components.database import Database
from server.recommender.components.recommender import get_recommendation, get_user_ratings, get_top_movies, get_movie_list, get_user_unrated_movies, get_similar_movies, get_similar, get_final_recommendations

@pytest.fixture
def sample_ratings_data():
    return pd.DataFrame({'rating': [5, 4, 3], 'movie_id': [101, 102, 103]})

@pytest.fixture
def sample_movies_data():
    return pd.DataFrame({'movie_id': [101, 102, 103], 'genre': ['Action', 'Comedy', 'Drama']})

@pytest.fixture
def sample_user_id():
    return 1

def test_get_user_ratings1(sample_ratings_data):
    with patch('server.recommender.components.database.Database.query', return_value=[(5, 101), (4, 102), (3, 103)]):
        ratings = get_user_ratings(sample_user_id)
        assert ratings.equals(sample_ratings_data)

def test_get_final_recommendations1(sample_movies_data):
    similar_movies = pd.DataFrame({'movie_id': [101, 102], 'similarity_coefficient': [0.5, 0.6]})

    final_list = get_final_recommendations(similar_movies)
    assert final_list is not None

@patch.object(Database, 'query')
def test_get_user_ratings2(mock_query):
    mock_query.return_value = [('4', '1'), ('5', '2')]
    result = get_user_ratings(1)
    expected_result = pd.DataFrame([('4', '1'), ('5', '2')], columns=["rating", "movie_id"])
    pd.testing.assert_frame_equal(result, expected_result)

@patch.object(Database, 'query')
def test_get_top_movies(mock_query):
    mock_query.return_value = [(5, '1'), (4, '2'), (5, '3')]  # ratings are now integers
    result = get_top_movies()
    expected_result = pd.DataFrame([('1', 5.0), ('3', 5.0), ('2', 4.0)], columns=["movie_id", "rating"]).to_json(index=False, orient="table")
    assert result == expected_result

@patch.object(Database, 'query')
def test_get_movie_list(mock_query):
    mock_query.return_value = [('1', 'Action,Adventure'), ('2', 'Comedy,Romance')]
    result = get_movie_list()
    expected_result = pd.DataFrame([('1', ['Action', 'Adventure']), ('2', ['Comedy', 'Romance'])], columns=["movie_id", "genre"])
    pd.testing.assert_frame_equal(result, expected_result)

def test_get_final_recommendations2():
    similar_movies = pd.DataFrame([('2', 0.0), ('3', 0.5)], columns=["movie_id", "similarity_coefficient"])
    result = get_final_recommendations(similar_movies)
    expected_result = pd.DataFrame([('3', 0.5), ('2', 0.0)], columns=["movie_id", "similarity_coefficient"]).to_json(index=False, orient="table")
    assert result == expected_result
