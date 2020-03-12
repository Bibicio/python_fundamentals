#formas de import
#from module import mod, mo2 - vc importa classes especificas daquele arquivo
#import module - dessa forma vc importa a pasta toda, zero especificaçao - essa ẽ a forma mais usada - pois te ajuda a saber de onde ta vindo, fazendo - faz_alguma_coisa = module.mod()
#from module import * - chama todo o module, mas quando chama, não precisa passar a classe module toda vez - porem é uma maneira relativamente errada
#site de ajuda: docs.python.org/3/library



# def mod():
#     print('mod')

# def mod2():
#     print('mod2')


# class modd():

#     def __init__(self):
#         self.__nome = 'modulo'
#         self.__teste = 'esse é o teste'
#     def mod(self):
#         print(self.__nome)

#     def mod2(self):
#         print('Mod 2')

# m1 = modd()
# m1.mod()

# for _ in range(12):
#     print(1)



# pip freeze 
# pip freeze > requirements.txt
# pip install -r requirements.txt


# import os #serve pra entrar em contato diretamente com o sistema operacional. Podendo incluir comanddos do SO

# print(dir(os))  
# print(os.getenv('HOME')) #FUNÇAO LINUX/WINDOWS
# print(os.getenv('USER')) #FUNÇAO LINUX/WINDOWS
# print(os.system('ls -lah'))

import sys

texto = 'palavra'


# print(range(len(texto))) 

# for i in len(texto): 
#     print(i) 


#nao tem como inteirar uma len numa unidade



# for i in range(len(sys.argv)): #range = contador
#     if i == 0:
#         print(f'função: {sys.argv[0]}')
#     else:
#         print(f'{i}. argumento: {sys.argv[i]}')
