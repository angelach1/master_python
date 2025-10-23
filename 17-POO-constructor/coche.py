class Coche:

    # Atributos o propiedades de la clase (variables de instancia)

    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Atributos de visibilidad, público y privado. Para hacer un atributo privado se usa __ antes del nombre
    soy_publico = "Soy un atributo público"
    __soy_privado = "Soy un atributo privado"


    # Constructor de la clase
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    # Métodos o funciones de la clase (comportamientos del objeto)

    def getPrivado(self):
        return self.__soy_privado

    def setColor(self, color):
        self.color = color  
    def getColor(self):
        return self.color
    
    def setMarca(self, marca):
        self.marca = marca
    def getMarca(self):
        return self.marca
    
    def setModelo(self, modelo):
        self.modelo = modelo
    def getModelo(self):
        return self.modelo

    def get_velocidad(self):
        return self.velocidad
    def set_velocidad(self, velocidad):
        self.velocidad = velocidad
 
    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        self.velocidad -= 10
    
    def getInfo(self):
        info = "------ INFORMACIÓN DEL COCHE ------\n"
        info += "Color: " + self.color + "\n"
        info += "Marca: " + self.marca + "\n"
        info += "Modelo: " + self.modelo + "\n"
        info += "Velocidad: " + str(self.velocidad) + " km/h\n"
        info += "Caballaje: " + str(self.caballaje) + " CV\n"
        info += "Plazas: " + str(self.plazas) + "\n"
        return info
 
    # Fin de la clase Coche