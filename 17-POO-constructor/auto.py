#clase coches
class Coche():
    #atributos o propiedades
    __color ="Rojo"
    __marca = "Ferrari"
    __modelo = "Aventador"
    __velocidad = 300
    __caballaje = 5000
    __plazas = 2
    
    #contructor de la clase
    
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.__color = color
        self.__marca =marca
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__caballaje = caballaje
        self.__plazas = plazas
    
    #metodos de la clase
    def setColor(self, color):
        self.__color = color
    
    def getColor(self):
        return self.__color
    
    def acelerar(self):
        self.__velocidad += 1
        
    def frenar(self):
        self.__velocidad -= 1
        
    def getVelocidad(self):
        return self.__velocidad
    
    def setModelo(self,modelo):
        self.__modelo = modelo
        
    def getModelo(self):
        return self.__modelo 
    
    def setMarca(self,marca):
        self.__marca = marca
        
    def getMarca(self):
        return self.__marca
    
    def setCaballaje(self,caballaje):
        self.__caballaje = caballaje
        
    def getCaballaje(self):
        return self.__caballaje
    
    def getInfo(self):
        info = "------Informacion del coche-----"
        info += "\n color: "    + self.getColor()
        info += "\n velocidad:" + str(self.getVelocidad())
        info += "\n Modelo :  " + self.getModelo()
        info += "\n Marca :   " + self.getMarca()
        info += "\n Caballaje :   " + str(self.getCaballaje())
        
        return info
    
    
        
 #fin creacion de la clase coche