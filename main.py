from Clases.menu import *
from Clases.basedatos import *
from Clases.parametro import *
def main():
    menu = Menu("Control Temperatura")
    op=menu.ver()
    if op =="1":
        menu2=MenuCaptura()
        op2=menu2.ver()
        if op2 =="1":
            CDatoR()
            control()
            menu3 = MenuRegreso()
            op3=menu3.ver()
            if op3 =="1":
                main()
            elif op3=="2":
                pass

        elif op2 =="2":
            grafica()
            control()
            menu3 = MenuRegreso()
            op3=menu3.ver()
            if op3 =="1":
                main()
            elif op3=="2":
                pass
        elif op2 =="3":
            main()
    
    elif op =="2":
            t=Rangos()
            t.GuardarR()
            menu3 = MenuRegreso()
            op3=menu3.ver()
            if op3 =="1":
                main()
            elif op3=="2":
                pass

    elif op =="3":
        menu2=MenuReportes()
        op2=menu2.ver()
        if op2 =="1":
            graficae()
            menu3 = MenuRegreso()
            op3=menu3.ver()
            if op3 =="1":
                main()
            elif op3=="2":
                pass
        elif op2 =="2":
            promedio()
            max()
            min()
            menu3 = MenuRegreso()
            op3=menu3.ver()
            if op3 =="1":
                main()
            elif op3=="2":
                pass
        elif op2 =="3":
            main()
        
        else:
            print("Opción inválida")
            main()
    

if __name__=='__main__':
    main()
