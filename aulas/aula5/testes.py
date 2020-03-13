# def somar(x, y):
#     return x + y

# def subtracao(x, y):
#     return x - y

# def multiplicacao(x, y):
#     return x * y


#     # Testar função somar
#     assert somar(2, 2) == 4, f"Obtido: {somar(2, 2)} Esperado: 4"
#     assert somar(3, 2) == 5, f"Obtido: {somar(3, 2)} Esperado: 5"

#     #testar subtracao
#     assert subtracao(3, 2) == 1, f"Obtido: {subtracao(3,2)} Esperado: 2"

#     #testar multiplicacao
#     assert multiplicacao(2, 2) == 4, f"obtido: {multiplicacao(2, 2)} Esperado: 4"




from unittest import TestCase, main

def somar(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y


    class Testes(TestCase):

        def test_soma(self):
            self.assertEqual(somar(5, 5), 10)
            self.assertEqual(type(somar(5, 5), int))
            self.assertIsNone(somar(5, 5), None)
            self.assertLess(somar(5, 5), 11)

        def test_sub(self):
            self.assertEqual(subtracao(10, 5), 5)
            self.assertEqual(type(subtracao(10, 5), int))
            self.assertIsNone(subtracao(10, 5), None)
            self.assertLess(subtracao(10, 5), 11)