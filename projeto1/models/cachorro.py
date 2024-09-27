class Cachorro:
    def __init__(self, nome, idade, raca, dono, tel):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.dono = dono
        self.tel = tel

listaCachorros = []

def addCachorro(cachorro):
    id = len(listaCachorros) +1
    novoCachorro = Cachorro(cachorro)
    listaCachorros.append(novoCachorro)


    