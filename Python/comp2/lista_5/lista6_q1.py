class Fracao():
    def __init__(self, numerador, denominador):
        try:
            self.__numerador = numerador
            self.__denominador = denominador
            res = self.__numerador/self.__denominador
        except ZeroDivisionError:
            print("\nDenominador inválido!")

    def getNumerador(self): return self.__numerador
    def getDenominador(self): return self.__denominador

    def __str__(self):
        return str('{} / {}'.format(self.__numerador, self.__denominador))

    def __add__(self, outro):
        num = (self.__numerador*outro.getDenominador()) + \
            (outro.getNumerador()*self.__denominador)
        den = self.__denominador * outro.getDenominador()
        return Fracao(num, den)

    def __sub__(self, outro):
        num = (self.__numerador*outro.getDenominador()) - \
            (outro.getNumerador()*self.__denominador)
        den = self.__denominador * outro.getDenominador()
        return Fracao(num, den)

    def __truediv__(self, outro):
        num = self.__numerador * outro.getDenominador()
        den = self.__denominador * outro.getNumerador()
        return Fracao(num, den)
