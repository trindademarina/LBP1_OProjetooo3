from flask import Blueprint, render_template, request

cachorro = Blueprint('cachorro', __name__)

@cachorro.route("/add", methods='POST')
def addCachorro():
    nome = request.form['nome']
    idade = request.form['idade']
    raca = request.form ['raca']
    dono = request.form ['dono']
    tel = request.form ['tel']


