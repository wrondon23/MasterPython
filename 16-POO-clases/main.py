
# Programacion orientada a objeto contrullendo una clase de ejemplo 

#clase coches

class Coche():
    #atributos o propiedades
    color ="Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 5000
    plazas = 2
    
    #metodos de la clase
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def acelerar(self):
        self.velocidad += 1
        
    def frenar(self):
        self.velocidad -= 1
        
    def getVelocidad(self):
        return self.velocidad
    
    def setModelo(self,modelo):
        self.modelo = modelo
        
    def getModelo(self):
        return self.modelo 
    
        
 #fin creacion de la clase coche
 
 #crear objeto y/o instanciar la clase 
 


carro = Coche()

carro.setColor("amarillo")

print(carro.marca, carro.getModelo(), carro.getColor())
print("Veloridad Actual",carro.getVelocidad())

carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.acelerar()

print("Veloridad nueva",carro.getVelocidad())

carro.frenar()
carro.frenar()

print("Veloridad nueva",carro.getVelocidad())

    

