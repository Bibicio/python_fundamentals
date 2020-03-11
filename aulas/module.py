#formas de import
#from module import mod, mo2 - vc importa classes especificas daquele arquivo
#import module - dessa forma vc importa a pasta toda, zero especificaçao - essa ẽ a forma mais usada - pois te ajuda a saber de onde ta vindo, fazendo - faz_alguma_coisa = module.mod()
#from module import * - chama todo o module, mas quando chama, não precisa passar a classe module toda vez - porem é uma maneira relativamente errada




def mod():
    print('mod')

def mod2():
    print('mod2')


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

for _ in range(12):
    print(1)



pip freeze 
pip freeze > requirements.txt
pip install -r requirements.txt