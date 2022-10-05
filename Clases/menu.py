class Menu:
    def __init__(self, control):
        self.control = control

    def ver(self):
        print("BIENVENIDO AL SISTEMA".center(50,"*"))
        print("1. Captura de datos")
        print("2. Configuración de parámetros")
        print("3. Reportes")
        op=input(">>>")

        return op


class MenuCaptura:
    def ver(self):
        print("MENU CAPTURA DE DATOS".center(20,"*"))
        print("Como desea realizar la captura de los datos?")
        print("1. Cantidad")
        print("2. Grafica")
        print("3. Regresar al menú principal")
        op=input(">>>")

        return op

class MenuReportes:
    def ver(self):
        print("MENU REPORTES".center(20,"*"))
        print("1. Grafica")
        print("2. Valores max, min y promedio")
        print("3. Regresar al menú principal")
        op=input(">>>")

        return op

class MenuRegreso:
    def ver(self):
        print("Desea volver al menú anterior?")
        print("1. Sí")
        print("2. No")
        op=input(">>>")

        return op


if __name__=='__main__':
     m= Menu("xxx")
     m.ver()
