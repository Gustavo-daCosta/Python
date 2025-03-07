from flask import Blueprint, request

outros = Blueprint(
    '/outros',
    __name__,
    url_prefix="/"
)

@outros.get("/ping")
def ping():
    return "pong"

@outros.route("/name", methods=['POST'])
def mostra_nome():
    dados = request.get_json()
    nome = dados["name"]
    pokemon = dados["pokemon"]
    
    if (nome is None or nome.strip() is "") or (pokemon is None or pokemon.strip() is ""):
        return {"error": "Parâmetros incompletos"}, 422
    
    return {"message": f"Olá {nome}, você escolheu o pokemon {pokemon}"}

