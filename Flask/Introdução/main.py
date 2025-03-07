from flask import Flask
from pomodoro.pomodoro import pomodoro
from outros.outros import outros

app = Flask(__name__)

app.register_blueprint(pomodoro)
app.register_blueprint(outros)
