#Herencias: es la posibilidad de compartir atributos y metodos entres clase. y que diferentes clases hereden de otras

#creando la clase persona

class Persona():
    
    #metodos get 
    def getNombre(self):
        return self.Nombre
    
    def getApellido(self):
        return self.Apellido
    
    def getAltura(self):
        return self.Altura
    
    def getEdad(self):
        return self.Edad
    
    #Metodos set
    
    def setNombre(self, Nombre):
        self.Nombre = Nombre
    
    def setApellido(self, Apellido):
        self.Apellido = Apellido
        
    def setAltura(self, Altura):
        self.Altura =  Altura
    
    def setEdad(self, Edad):
        self.Edad = Edad
    
    #metodos de acciones
    
    def hablar(self):
        return "Estoy hablando" 
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"   
    

class Informatico(Persona):
    
    #constructor  
    def __init__(self):
        self.lenguaje = "HTML, CSS, JavaScript. PHP"
        self.experiencia = 5
        
    #metodos lenguasjes
    def getLenguajes(self):
        return self.lenguaje
    
    def setAprender(self,lenguajes):
        self.lenguaje = lenguajes
        return self.lenguaje
        
    def  programar(self):
        return "Estoy programando"
        