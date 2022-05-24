from deportista import Deportista
from persona import Persona
class Futbolista(Deportista):
    _listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        super().__init__(nombre,edad,altura,sexo,"Futbol",añosPracticando)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        Futbolista._listaFutbolistas.append(self)
    
    #metodos get y set

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self,nuevo):
        self._golesMarcados=nuevo
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setTarjetasRojas(self,nuevo):
        self._tarjetasRojas=nuevo
    
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setPiernaHabil(self,nuevo):
        self._piernaHabil=nuevo

    #metodos get y set para la lista de futbolistas

    @classmethod
    def getListaFutbolistas(cls):
        cls._listaFutbolistas

    @classmethod
    def setListaFutbolistas(cls,nuevo):
        cls._listaFutbolistas=nuevo

    #otro metodo
    def __str__(self):
        return "Mi nombre es "+ self.getNombre() +" soy profesional en el deporte "+ self.getDeporte() +" Tengo "+str(self.Edad())+" años de edad y llevo "+str(self.getAñosPracticando())+" años en el deporte"





    

