from sqlalchemy import select
from core import user_table


# Select
selecione = select([user_table])
print([x for x in selecione.execute()]) #isto é uma compreensão em lista - vide exemplos em baixo


# Select com filtro
filtro = input('digite o nome do usuario:')

selecione_filtro = select([user_table]).where(user_table.c.nome == filtro)

print([f for f in selecione_filtro.execute()])


#uma compreensao em lista, é basicamente um for/if/while dentro de uma lista.

#exemplo
# lista = [i*2 for i in range(100)] #tem um i a mais, mas esse i que está a mais é o i que vai ficar dentro da lista
# for i in range(10):
#     lista.append(i * 2)

# print(lista)