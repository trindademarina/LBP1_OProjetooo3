
class Usuario:
    def __init__(self, nome, senha,): #tipo
        self.nome = nome
        self.senha = senha


users = []

user1=Usuario("user1","20")
users.append(user1)

def verificacao(user, senha):
    for u in users: 
        if (u.nome == user and u.senha == senha):
            return u.tipo
    return None
        

