from flask import Flask, request
import sys

test = [ #REMOVER
    {  # exemplo de retorno
        "id": "0",
        "Name": "jeremias"
    },
    {
        "id": "1",
        "Name": "jessica"
    }
]

app = Flask(__name__)


@app.route("/<id>", methods=['GET'])  #Fazendo requisição diretamente pelo link. Exemplo: 127.0.0.1:5000/<Id_Usuario>
def home(id):
    for user in test:
        if user['id'] == id:
            return user['Name']


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
