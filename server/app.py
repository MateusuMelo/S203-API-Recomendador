from flask import Flask, json
from recommender.components.recommender import Recommender

db_file = "./db.sqlite3"
r = Recommender(db_file)

app = Flask(__name__)

@app.route("/recommend/<id_user>", methods=['GET'])  # Fazendo requisição diretamente pelo link. Exemplo: 127.0.0.1:5000/<Id_Usuario>
def recommend(id_user):
    rec = r.get_recommendation(id_user)
    # Retorna um array vazio caso não existam recomendações para este usuário
    return [] if not rec else json.loads(rec)


@app.route("/similar/<id_movie>", methods=['GET'])  # Fazendo requisição diretamente pelo link. Exemplo: 127.0.0.1:5000/<Id_Usuario>
def similar(id_movie):
    sim = r.get_similar(id_movie)
    # Retorna um array vazio caso não existam recomendações para este usuário
    return [] if not sim else json.loads(sim)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
