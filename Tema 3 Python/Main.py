from Operador import *
from OperadorAbstracto import *

if __name__ == '__main__':
    print("Método de clase")
    print("Pruebas Abisai")
    print(Operador.OperadorSobrecarga(80,100,120,140,160,180))

    print("")

    print("Método de instancia")
    print("Pruebas Abisai")
    prueba = Operador(80,100,120,140,160,180)
    print(prueba.get_totalUnidades())

    print("")

    print("Clase abstracta")
    print("Pruebas Abisai")
    print(OperadorAbstracto.OperadorAbstracto(80,100,120,140,160,180))

    print("")

    print("Sobrecarga de operadores")
    print("Pruebas Abisai")
    prueba2 = Operador(80,100,120,140,160,180)
    print("Sobrecarfga str")
    print(prueba2.__str__())