from flask import Blueprint, render_template, request
from .cachorro import verificacao

cachorro = Blueprint('cachorro', __name__)

@cachorro.route("/login", methods=['POST'])
def index():
        user = request.form['user']
        senha = request.form['senha']
        resultado = verificacao(user, senha)
        if resultado == None:
                return #erro
        return render_template('login.html')


