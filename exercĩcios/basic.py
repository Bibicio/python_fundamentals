#exercicio 1
#nome = input("digite seu nome")
#print("meu nome ẽ",nome)

#exercicio 2
#dado a lista:
#times = (['corinthians', 'palmeiras', 'são paulo' ], ['preto','branco', 'verde', 'vermelho'])

#tentativa
#times[0] = 'corinthians
#times[1] = 'palmeiras'
#times[2] = 'são paulo'
#times[3] = 'preto'
#times[4] = 'branco'
#times[5] = 'verde'
#times[6] = 'vermelho'
#print((times[0]) + (times[3]) (times[4]))
#print('corinthians' in times)

#jeitos de fazer

# times = [['Corinthians', 'Palmeiras', 'São Paulo'], ['Preto', 'Branco', 'Verde', 'Vermelho']]

# imprima na tela as seguintes mensagens:

# time: <nome_time>, cores: <cores_time>

# for i in times[0]:
#     for n in times[1]:
#         if times[0][0] == 'Corinthians':
#             cor1, cor2 = 'Preto', 'Branco'
#             print(f'time: {i} Cores: {cor1} {cor2}')

#exercicio 3
#dado o dicionario

#dado = {    
#   'estados': {
#        'sp': {
#            'nome': 'são paulo',
#            'municipios': 645,
#            'populaçao': 44.04
#        },
#        'rj': {
#            'nome': 'rio de janeiro',
#            'municipios': 92,
#            'populaçao': 16.72
#        },
#        'mg': {
#            'nome': "minas gerais",
#            'municipios': 31,
#            'populaçao': 29.87
#        }
#      }}
    #imprima na tela as seguintes mensagens
    #Estado: <nome_estado>
    #municipios: <nome_municipio>
    #populaçao: <nome_popualaçao>

# print(f"Estado: {dados['estados']['sp']['nome']}")
# print(f"Municipios: {dados['estados']['sp']['municipios']}")
# print(f"População: {dados['estados']['sp']['populacao']}")

# print(f"Estado: {dados['estados']['rj']['nome']} \nMunicipios: {dados['estados']['rj']['municipios']} \nPopulação: {dados['estados']['rj']['populacao']}")

#for estado in dados['estados'].keys():
#    print(f"Estado: {dados['estados'][estado]['nome']}")
#    print(f"Municipios: {dados['estados'][estado]['municipios']}")
#    print(f"População: {dados['estados'][estado]['populacao']}")
#    print(' ')


