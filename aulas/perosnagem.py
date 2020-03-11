#-*- coding: UTF-8 -*-

class personagem():

    def __init__(self):
        self.nome = 'Alucard'
        self.idade = 120
        self.vida = 100

p1 = personagem()
p2 = personagem()

print(p1.nome, p1.idade, p1.vida)
print(p2.nome, p2.idade, p2.vida)