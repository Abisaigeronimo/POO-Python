from abc import abstractmethod
from abc import ABCMeta

class Operador1(metaclass=ABCMeta):
    _cantidadUnidades = float(0)
    _totalUnidades = float(0)

    @abstractmethod
    def Operador1(self, lunes, martes, miercoles, jueves, viernes, sabado):
        pass

    @abstractmethod
    def getOperador(self):
        pass
