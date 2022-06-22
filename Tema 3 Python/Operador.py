class Operador:

    __lunes = int(0)
    __martes = int(0)
    __miercoles = int(0)
    __jueves = int(0)
    __viernes = int(0)
    __sabado = int(0)
    __cantidadUnidades = int(0)
    __totalUnidades = int(0)


    def __init__(self, lunes, martes, miercoles, jueves, viernes, sabado):
        self.__lunes = lunes
        self.__martes = martes
        self.__miercoles = miercoles
        self.__jueves = jueves
        self.__viernes = viernes
        self.__sabado = sabado
        self.__cantidadUnidades = lunes + martes + miercoles + jueves + viernes + sabado
        self.__totalUnidades = self.__cantidadUnidades / 6

        if (self.__totalUnidades >= 100):
            print("Recibirás tus incentivos")
        else:
            print("No recibirás tus incentivos")

    def get_totalUnidades(self):
        return self.__totalUnidades

    @staticmethod
    def OperadorSobrecarga(lunes, martes, miercoles, jueves, viernes, sabado):
        cantidadUnidades = lunes + martes + miercoles + jueves + viernes + sabado
        totalUnidades = cantidadUnidades / 6

        if (totalUnidades >= 100):
            print("Recibirás tus incentivos")
        else:
            print("No recibirás tus incentivos")

        return totalUnidades

    def __str__(self):
        return str(self.__totalUnidades)