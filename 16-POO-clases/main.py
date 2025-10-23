# Programación Orientada a Objetos (POO) en Python

# Definición de una clase (plantilla para crear objetos)
class Coche:

    # Atributos o propiedades de la clase (variables de instancia)

    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Métodos o funciones de la clase (comportamientos del objeto)

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
 
    # Fin de la clase Coche

# Crear un objeto / instancia de la clase Coche
mi_coche = Coche()

# Usar los métodos del objeto
mi_coche.setColor("Azul")

print('---------"Características del coche 1:" ---------')

print(mi_coche.getMarca(), mi_coche.getModelo(), mi_coche.getColor())


print("Velocidad inicial:", mi_coche.get_velocidad())
mi_coche.acelerar()
print("Velocidad después de acelerar:", mi_coche.get_velocidad())
mi_coche.frenar()
print("Velocidad después de frenar:", mi_coche.get_velocidad())

# Crear otro objeto / instancia de la clase Coche
mi_coche2 = Coche()

print('--------- "Características del coche 2:" ---------')

mi_coche2.setColor("Verde")
mi_coche2.setMarca("Toyota")
mi_coche2.setModelo("Corolla")
print(mi_coche2.getMarca(), mi_coche2.getModelo(), mi_coche2.getColor())
print("Velocidad inicial:", mi_coche2.get_velocidad())
mi_coche2.acelerar()
mi_coche2.acelerar()
print("Velocidad después de acelerar:", mi_coche2.get_velocidad())
print(type(mi_coche2))  # Muestra el tipo del objeto
print(dir(mi_coche2))   # Muestra los atributos y métodos del objeto
print("Número de caballos:", mi_coche2.caballaje)  # Acceso directo a un atributo
print("Número de plazas:", mi_coche2.plazas)  # Acceso directo a un atributo

print("Fin del programa.")
