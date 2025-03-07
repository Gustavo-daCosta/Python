from flask import Blueprint, request

pomodoros = [
    {
        "name": "Murilo",
        "pomodoro": "Montar a aula de hoje"
    },
    {
        "name": "Heitor",
        "pomodoro": "Almoço"
    }
]

pomodoro = Blueprint(
    'pomodoro',
    __name__,
    url_prefix="/pomodoro"
)

@pomodoro.route("/listar", methods=["GET"])
def pegar_pomodoros():
    return {"pomodoros": pomodoros}

@pomodoro.route("/criar", methods=["POST"])
def criar_pomodoros():
    dados = request.get_json()
    nome = dados.get("name")
    pomodoro = dados.get("pomodoro")
    
    if (nome is None) or (pomodoro is None):
        return {"error": "Campos incorretos"}, 422
    
    registro = {
        "name": nome,
        "pomodoro": pomodoro
    }
    
    pomodoros.append(registro)
    return registro
