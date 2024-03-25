import math

class ErroAritimetico(Exception): pass
class RaizNegativa(ErroAritimetico): pass
class ModuloMaior(ErroAritimetico):pass


def raizQuadrada(num):
    if num > 0: return math.sqrt(num)
    else: raise RaizNegativa

def modulo(a,b):
    if a > b: return a % b
    else: raise ModuloMaior


try:
    raizQuadrada(81)
    raizQuadrada(-9)
    modulo(8,3)
    modulo(3,8)
except RaizNegativa: print("Raiz Negativa!")
except ModuloMaior: print("Modulo Maior")