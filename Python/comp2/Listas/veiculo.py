class veiculo:
    def __init__(self, marca, modelo, dono, tanque_capacid, 
    tanque_atual, autonomia_km_l, km_rodados):
        self.marca = marca
        self.modelo = modelo
        self.dono = dono
        self.__tanque_capacid = tanque_capacid
        self.__tanque_atual = tanque_atual
        self.__autonomia_km_l = autonomia_km_l
        self.__km_rodados = km_rodados
        self.__validarProp(autonomia_km_l)
        self.__validarProp(tanque_capacid)
    def lerTanqueAtual(self):
        return self.__tanque_atual
    def lerTanqueCapacid(self):
        return self.__tanque_capacid
    def lerAutonomia(self):
        return self.__autonomia_km_l
    def lerRodagem(self):
        return self.__km_rodados
    def alterarAutonomia(self, valor_autonomia):
        if (self.__validarProp(valor_autonomia) == True):
            self.__autonomia_km_l = valor_autonomia
            return True
        else:
            return False
    def abastercerTanque(self,litros):
        if (self.__validarProp(litros) == True):
            if (litros + self.__tanque_atual <= self.__tanque_capacid):
                self.__tanque_atual += litros
                return True
            else: return False
        else: return False
    def fazerViagem(self, km):
        if(km / self.__autonomia_km_l <= self.__tanque_atual):
            self.__tanque_atual -= (km / self.__autonomia_km_l)
            self.__km_rodados += km
            return True
        else: return False
    def __validarProp(self, valor):
        if (valor >= 0): return True
        else: return False
