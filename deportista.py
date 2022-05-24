from persona import Persona
class Deportista(Persona):
    def __init__(self,nombre,edad,altura,sexo,deporte,añosPracticando):
        super().__init__(nombre,edad,altura,sexo)
        self._deporte=deporte
        self._añosPracticando=añosPracticando

#metodos get y set
def getDeporte(self):
        return self._deporte
def setDeporte(self,nuevo):
        self._deporte=nuevo

def getAñosPracticando(self):
        return self._añosPracticando
def setAñosPracticando(self,nuevo):
        self._añosPracticando=nuevo

    
