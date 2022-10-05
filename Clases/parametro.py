from .basedatos import *

class Temperatura():
    def __init__(self,HipoMin,HipoMax,NormalMin,NormalMax,FiebreMin,FiebreMax):
        self.HipoMin=float(HipoMin)
        self.HipoMax=float(HipoMax)
        self.NormalMin=float(NormalMin)
        self.NormalMax=float(NormalMax)
        self.FiebreMin=float(FiebreMin)
        self.FiebreMax=float(FiebreMax)
        self._file="C:/Users/lala_/OneDrive/Documentos/Octavo Semestre/DABM/Lab 3/Databases/Rangos.csv"
    
    def GuardarR(self):
        file=open(self._file,"w")
        datos=str(self.HipoMin) +";"+str(self.HipoMax)+";"+str(self.NormalMin)+";"+str(self.NormalMax)+";"+str(self.FiebreMin)+";"+str(self.FiebreMax)+"\n"
        file.write(datos)
        file.close()
    

def Rangos():
    
    HipoMin=input("El minimo para hipotermia es: ")
    HipoMax=input("El maximo para hipotermia es: ")
    NormalMin=input("El minimo para normal es: ")
    NormalMax=input("El maximo para normal es: ")
    FiebreMin=input("El minimo para fiebre es: ")
    FiebreMax=input("El maximo para fiebre es: ")
      
    t = Temperatura(HipoMin,HipoMax,NormalMin,NormalMax,FiebreMin,FiebreMax)
    return t

def control():
    a = open("C:/Users/lala_/OneDrive/Documentos/Octavo Semestre/DABM/Lab 3/Databases/Rangos.csv", "r")
    datos = a.readlines()
    for t in datos:
        rangos = t.split(";")
        print(Vt)
        for i in Vt:
            if i >= float(rangos[0]) and i <= float(rangos[1]):
                temp ="H"
            elif i >= float(rangos[2]) and i <=float(rangos[3]):
                temp ="N"
            elif i >= float(rangos[4]) and i <=float(rangos[5]):
                temp ="F"
            else:
                pass
            print("Categoría=",temp)
            p.write(temp.encode())

            

