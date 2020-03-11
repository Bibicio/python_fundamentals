#-*- coding: UTF-8 -*-
# class automovel(): #classe py

#     def _init_(self):
#         self.motor = 'conbustao'




# class carro(): #classe py


#     def __init__(self):
#         automovel.__init__(self)
#         self.rodas = 4 
#         self.porta_mala = 'normal'
#         self.motor = True
#         self.volante = True
#         self.tanque = True
    
#     def ligar (self):
#         print('carro ligado')

#     def desligar(self):
#         print('carro desligado')

#     def acelerar(self):
#         print('acelerando')

#     def frear(self):
#         print('freando')

# #criando a variavel, criando o objeto dentro da classe
# #carro01 = carro()
# #objeto = classe()
# # hilux = carro()

# #dando os comandos pro carro funcionar
# # carro01.ligar()
# # carro01.acelerar()
# # carro01.frear()
# # carro01.desligar()  

# class Fiat147(carro):

#     def __init__(self):
#         carro.__init__(self)
#         super().__init__() #ele puxa o init da classe py la de cima
#         self.motor = 'eletrico'
#         self.porta_mala = 'com agua'

# c001 = Fiat147() #parenteses pq estã instanciando uma classe
# print(c001.motor)


class Pai():
    hobby = 'programar'
    def _init_(self):
        self.profissao = 'advogado'

    def mudarProfissao(self, nova_profissao):
        self.profissao = nova_profissao

    def mudarHobby(self):
        self.hobby = 'jardineiro'


joao = Pai()
joao.mudarProfissao('carpinteiro')
joao.mudarHobby()
print(joao.profissao)
print(joao.hobby)


# class Mae(): #tudo que esta fora do init, precisa iniciar
#         self.hobby = 'vender miçanga'

#     def _init_(self):
#         self.profissao = 'medica'

# class Filho(Pai, Mae):

    # def __init__(self):
    #     Pai.__init__(self)
    #     Mae.__init__(self) #ele vai pegar desse aqui, pois o pai foi subescrevido
    #     self.estudo = 'programação' #se eu colocar profissao no lugar de estudo, eu mudo, pois ele deixa de herdar a profissao  dos pais


# José = Filho()

# print(José.profissao)