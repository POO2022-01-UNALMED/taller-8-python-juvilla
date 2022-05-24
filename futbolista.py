from deportista import Deportista
from persona import Persona

class Futbolista(Deportista):

    _listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,goles,rojas,pierna):
        super().__init__(nombre,edad,altura,sexo,"Futbol",añosPracticando)
        self._golesMarcados=goles
        self._tarjetasRojas=rojas
        self._piernaHabil=pierna
        Futbolista._listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self,goles):
        self._golesMarcados=goles
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self,tarjeta):
        self._tarjetasRojas=tarjeta
    
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setPiernaHabil(self,pierna):
        self._piernaHabil=pierna

    @classmethod
    def getListaFutbolistas(cls):
        cls._listaFutbolistas

    @classmethod
    def setListaFutbolistas(cls,fut):
        cls._listaFutbolistas=fut

    def __str__(self):
        return "Mi nombre es "+ self.getNombre() +" soy profesional en el deporte "+self.getDeporte()+" Tengo "+str(self.getEdad())+" años de edad y llevo "+str(self.getAñosPracticando())+" años en el deporte"
    