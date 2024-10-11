from flask import Blueprint, render_template, request

cachorro = Blueprint('cachorro', __name__)

@cachorro.route("/login", methods=['POST'])
def index():
        user = request.form['user']
        senha = request.form['senha']
        return render_template('login.html')


