# Comentário

from Python.comp2.veiculo import veiculo
import unittest
print("Hello World")  # Imprimir algo na tela

# Variáveis

a = 4
b = "Dios Mio"

# Especificando variáveis

string = str(14)  # '14'
inteiro = int(14)  # 14
flutuante = float(14)  # 14.0

print(type(a))  # saber o tipo da variável

# Defininfo caracteres

nome = "Davi"
# é igual a
nome = 'Davi'

# Operadores Booleanos

if 2 < 6:
    print("2 menor que 6")
else:
    print("2 não é menor que 6")

# Lista

lista = ["1", "2", "3"]

# Tuplas

tupla = ("4", "5", "6")

# Dicionários

dict = {
    "Davi": 14,
    "Lannes": 1,
    "Amaral": 7
}

# Teste Unitário

"""
(self, marca, modelo, dono, tanque_capacid,tanque_atual, autonomia_km_l, km_rodados)
"""


class TestVeiculo(unittest.TestCase):
    def test_lerTanqueAtual(self):
        car1 = veiculo('Fiat', 'Siena', 'Carlos', 80, 0, 5, 0)
        self.assertEqual(car1.lerTanqueAtual(), 0)


if __name__ == "__main__":
    unittest.main()
