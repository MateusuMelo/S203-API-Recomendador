from flask import Flask, json
import sys
from recommender.components.recommender import get_recommendation

app = Flask(__name__)

@app.route("/<id>", methods=['GET'])  #Fazendo requisição diretamente pelo link. Exemplo: 127.0.0.1:5000/<Id_Usuario>
def home(id):
    movies = {"movies_id_list":json.loads(get_recommendation(id))}
    return movies

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
