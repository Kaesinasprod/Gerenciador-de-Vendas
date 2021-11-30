#Classe Cliente
#Contém os atributos dos clientes

class Cliente():
    def __init__(self, id, nome, endereco, telefone):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def print(self):
        print(self.id, self.nome, self. endereco, self.telefone)
        