from flask import Blueprint, render_template, redirect, url_for, request,session, make_response, flash, abort
from models.model import listaUsuarios
projeto = Blueprint('projeto', __name__)

@projeto.route("/")
def index():
    return render_template('index.html')

@projeto.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        for usuario in listaUsuarios:
            if request.form['user']== usuario.user and request.form['senha'] == usuario.senha:
                session['idUser'] = usuario.id #por segurnaça, add o id
                return redirect(url_for('projeto.dash')) 
        flash('Usuário ou senha incorretos!', 'error')  
        #abort(401) 
    return render_template('login.html')


@projeto.route("/dashboard")
def dash():
   return render_template('dashboard.html')


@projeto.route("/logout")
def logout():
   session.pop('idUser', None)
   flash('Logout bem sucedido!', 'success')
   return redirect(url_for('projeto.index'))

rotas_publicas = ['projeto.index', 'projeto.login']

@projeto.before_request
def verificarLogin():
    if request.endpoint == 'projeto.login' and 'idUser' in session:
        flash('Você ja esta logado', 'success')
        return redirect(url_for('projeto.dash')) #ja estou logado e vou pro dash
    
    if request.endpoint in rotas_publicas:
        return
    
    if 'idUser' not in session:
        abort(401)
        return redirect(url_for('projeto.login'))
    return

@projeto.errorhandler(401)
def acessoNegado (e):
    return render_template('401.html'), 401

@projeto.errorhandler(403)
def acessoproibido (e):
    return render_template('403.html'), 403

@projeto.route('/admin')
def admin():
    if session['idUser'] != 1:
        abort(403)
    return render_template('admin.html')


# @projeto.route('/cookie')
# def cookies():
#     resp = make_response('cookie criado,"na teoria"')
#     resp.set_cookie('username','')
#não foi feito os cookies pois não entendi nada, porém vou me dedicar a entender.


