#dado o dicionario

produtos = dict(produtos=dict(p1=dict(nome="Camiseta Star Wars", preco=99.90), p2=dict(nome='Caneca Ricky&Morty', preco=49.90), p3=dict(nome='Camiseta SpiderMan', preco=69.90)))
#apartir do id do pruduto mostraremos o nome e o preco
#caso o produto nao exista mostraremos a seguinte mensagem: produto inexistente

#tentativa = 
# try:
#     id = p1 = 'camiseta star wars 99.90'
#     p2 = 'caneca ricky&morty 49.90'
#     p3 = 'camiseta spider man preco 69.90'
#     id_produto = input('digite o id do produto')
#     if id_produto not in produtos:
#         raise ValueError('produto inexistente')
#     else:
#         print('produto encontrado')
# except ValueError as e:
#     print (e)

#jeito certo
try:
    id_produto = input('digite o id do produto')
    if id_produto not in produtos('produtos'):
            raise ValueError('produto inexistente')
    else:
        print(f'Produto: {produtos['produtos'][id_produto]['nome']}')
        print(f 'preco: {produtos[produtos'