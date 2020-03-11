#Crie uma classe Mamĩfero com os atributos:
#   bebe leite

#crie uma classe homosapiens com os atributos
#   polegares = true
#   formaCaminhar = 'bipede'
#mẽtodo:
#   caça
#   comer
#   dormir
#   construir

#EU QUE FIZZZZZ AAAAAAAAAAAA
class Mamĩfero():

    def __init__(self):
        self.bebeLeite = True


class homosapiens(Mamĩfero):

    def __init__(self):
        super().__init__() #não precisa disso pois eu identei la em cima que homosapiens faz parte da classe mamifero
      #  Mamĩfero().__init__() #outra opçao, porem especifica
        self.polegares = True
        self.formaCaminhar = 'bípede'

    def caçar(self):
        print('caçando')
    def comer(self):
        print('comendo')
    def dormir(self):
        print('dormindo')
    def construir(self):
        print('construindo')

human = homosapiens() #sempre estanciar, guardar numa variavel

human.caçar()
human.comer()
human.dormir()
human.construir()
print(human.polegares)
print(human.formaCaminhar)
print(human.bebeLeite)
