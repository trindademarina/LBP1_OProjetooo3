class Usuario:
    def __init__(self, id, user, senha):
        self.id = id
        self.user = user
        self.senha = senha 

listaUsuarios = []

listaUsuarios.append(Usuario(1,'Admin', 'senha'))
listaUsuarios.append(Usuario(2,'User', 'senha2'))
