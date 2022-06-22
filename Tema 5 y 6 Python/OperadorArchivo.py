from abc import ABCMeta


class OperadorArchivo(ABCMeta):

    @staticmethod
    def OperadorAbstracto(lunes, martes, miercoles, jueves, viernes, sabado):
        cantidadUnidades = lunes + martes + miercoles + jueves + viernes + sabado
        totalUnidades = cantidadUnidades / 6

        if totalUnidades >= 100:
            print("Recibirás tus incentivos")
        else:
            print("No recibirás tus incentivos")

        return totalUnidades


class Archivos:

    def leerArchivo(self, archivo):
        file = open(archivo, 'r')
        lineas = []
        lineas_archivo = []
        for linea in file.readlines():
            lineas.append(linea.replace('\n', '').split(";"))
        file.close()
        for f in range(0, len(lineas)):
            try:
                lineas_archivo.append([int(lineas[f][0]), int(lineas[f][1]), int(lineas[f][2]), int(lineas[f][3]),
                                       int(lineas[f][4]), int(lineas[f][5])])
            except ValueError:
                lineas_archivo.append([0, 0, 0, 0, 0, 0])
            return lineas_archivo

    def calcularOperador(self, lista):
        resultados = []
        for f in range(0, len(lista)):
            resultados.append(OperadorArchivo.OperadorAbstracto(lista[f][0], lista[f][1], lista[f][2], lista[f][3],
                                                                lista[f][4], lista[f][5]))
            return resultados

    def guardarResultados(self, entrada, resultados):
        file = open("resultados.txt", 'w')
        file.write('Lunes#Martes#Miercoles#Jueves#Viernes#Sabado#Intensivos\n')
        for f in range(0, len(entrada)):
            linea = str(entrada[f][0]) + '#' + str(entrada[f][1]) + '#' + str(entrada[f][2]) + '#' + str(
                entrada[f][3]) + '#' + str(entrada[f][4]) + '#' + str(entrada[f][5]) + '#' + str(resultados[f]) + '\n'
            file.write(linea)
        file.close()


if __name__ == "__main__":
    prueba = Archivos()
    archivo = []
    archivo = prueba.leerArchivo("datos.txt")
    print(archivo)
    resultado = prueba.calcularOperador(archivo)
    print(resultado)
    prueba.guardarResultados(archivo, resultado)
