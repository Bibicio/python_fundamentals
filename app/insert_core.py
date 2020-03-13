from core import user_table, engine

con = engine.connect()
insert = user_table.insert()


#com input ficaria automatico, a pessoa inseria os dados e os dados ja ficam salvos em cada entrada; a forma a baixo é a forma manual, porem, pratica para poucos dados
# new = insert.values(idade=25, nome='Caio', senha='abacaxi123')
# con.execute(new)

con.execute(user_table.insert(), [
    {'nome':'marcelo', 'idade':20, 'senha':'limao321'},
    {'nome':'gustavo', 'idade':18, 'senha':'goiaba123'},
    {'nome':'guilherme','idade':22, 'senha':'maracuja456'}

])
