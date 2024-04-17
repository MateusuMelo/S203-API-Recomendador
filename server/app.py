from flask import Flask, json
import sys
from recommender.components.recommender import get_recommendation, get_similar

app = Flask(__name__)

@app.route("/recommend/<id_user>", methods=['GET'])  #Fazendo requisição diretamente pelo link. Exemplo: 127.0.0.1:5000/<Id_Usuario>
def recommend(id_user):
    movies = {"movies_id_list":json.loads(get_recommendation(id_user))}
    return movies

@app.route("/similar/<id_movie>", methods=['GET'])  #Fazendo requisição diretamente pelo link. Exemplo: 127.0.0.1:5000/<Id_Usuario>
def similar(id_movie):
    movies = {"movies_id_list":json.loads(get_similar((id_movie)))}
    return movies

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
