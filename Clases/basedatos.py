import serial 
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

global p
global Vt
p = serial.Serial('COM3',9600)
Vt = []
pausa = False

class BaseDatos:
    file = "C:/Users/lala_/OneDrive/Documentos/Octavo Semestre/DABM/Lab 3/Databases/DatosT.csv"

    def __init__(self,Nombre,Temperatura, Fecha, Hora):
        self.Nombre = Nombre
        self.Temperatura = float(Temperatura)
        self.Fecha = Fecha
        self.Hora = Hora


def CDatoR():
    print("Monitorización de temperatura de un paciente ")
    Cantidad = int(input("Ingrese la cantidad de datos que desea recoger: "))
    Nombre = input("Nombre del paciente: ")
    Fecha = time.strftime("%x")
    Hora = time.strftime("%X")
    for i in range(Cantidad):
        Temperatura = float(p.readline().decode().strip())
        Vt.append(Temperatura)
        a = open("C:/Users/lala_/OneDrive/Documentos/Octavo Semestre/DABM/Lab 3/Databases/DatosT.csv", "a")
        a.write(";".join([Nombre,str(Temperatura),Fecha,Hora])+"\n")
    a.close()
    return Vt 

 
def grafica():
    Nombre = input("Nombre del paciente: ")
    Fecha = time.strftime("%x")
    Hora = time.strftime("%X")
    try:
        p.close()
        p.open()
        print("Port is open")
    except:
        print("Problemas abriendo puerto")

    def onclick(event):
        global pausa
        print("Pausa")
        pausa= True

    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event', onclick)

    def update_data(i):
        if not pausa:
            punto = float(p.readline().decode().strip())
            b = open("C:/Users/lala_/OneDrive/Documentos/Octavo Semestre/DABM/Lab 3/Databases/DatosT.csv", "a")
            b.write(";".join([Nombre,str(punto),Fecha,Hora])+"\n")
            #print(punto)
            Vt.append(punto)
            ax.clear()
            ax.plot(Vt)
        b.close()
            

    ani = animation.FuncAnimation(fig,update_data)
    plt.show()
    print("Cerrar la ventana de la grafica")
    

def promedio():
    suma = 0
    for k in Vt:
            suma = suma + k
            prom = suma/(len(Vt))
    print("El valor promedio de temperatura es:" +str(prom))

def max():
    may = Vt[0]
    for l in Vt:
        if l > may:
            may = l
    print("El valor maximo de temperatura es:" +str(may))

def min():
    men = Vt[0]
    for j in Vt:
        if j < men:
            men = j
    print("El valor minimo de temperatura es:" +str(men))

def graficae():
    plt.title("Datos temperatura")
    plt.plot(Vt, color="red")
    plt.show()