class Persona:
    def __init__(self,nombre,edad,altura,sexo):
        self._nombre=nombre
        self._edad=edad
        self._altura=altura
        self._sexo=sexo

    def getNombre(self):
        return self._nombre
    
    
    def setNombre(self,nuevo):
        self._nombre=nuevo
    
    def getEdad(self):
        return self._edad

    def setEdad(self,nuevo):
        self._edad=nuevo

    def getAltura(self):
        return self._altura

    def setAltura(self,nuevo):
        self._altura=nuevo

    def getSexo(self):
        return self._sexo

    def setSexo(self,nuevo):
        self._sexo=nuevo
        