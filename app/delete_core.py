from sqlalchemy import delete
from core import user_table, engine


con = engine.connect()

nome = input('Digite o nome do usuario que será deletado:')

apaga = delete(user_table).where(user_table.c.nome == nome) #.c = column; ja é uma sintaxe do proprio python

resultado = con.execute(apaga)
print(resultado.rowcount)