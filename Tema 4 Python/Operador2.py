from Operador.Operador1 import Operador1


class Operador2(Operador1):
    __lunes = float(0)
    __martes = float(0)
    __miercoles = float(0)
    __jueves = float(0)
    __viernes = float(0)
    __sabado =   float(0)

    def __init__(self, lunes, martes, miercoles, jueves, viernes, sabado):
        self.__lunes = lunes
        self.__martes = martes
        self.__miercoles = miercoles
        self.__jueves = jueves
        self.__viernes = viernes
        self.__sabado = sabado
        self.Operador1()


    def Operador1(self):
        self.__cantidadUnidades = self.__lunes + self.__martes + self.__miercoles + self.__jueves + self.__viernes + self.__sabado
        self.__totalUnidades = self.__cantidadUnidades / 6

        if (self.__totalUnidades >= 100):
            print("Recibirás tus incentivos")
        else:
            print("No recibirás tus incentivos")
        self._totalUnidades = self.__totalUnidades

    def getOperador(self):
        return self._totalUnidades