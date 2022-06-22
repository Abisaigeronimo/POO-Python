from abc import ABC

class OperadorAbstracto(ABC):

    @staticmethod
    def OperadorAbstracto(lunes, martes, miercoles, jueves, viernes, sabado):
        cantidadUnidades = lunes + martes + miercoles + jueves + viernes + sabado
        totalUnidades = cantidadUnidades / 6

        if (totalUnidades >= 100):
            print("Recibirás tus incentivos")
        else:
            print("No recibirás tus incentivos")

        return totalUnidades