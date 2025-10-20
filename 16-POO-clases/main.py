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

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        self.velocidad -= 10
    def get_velocidad(self):
        return self.velocidad

    # Fin de la clase Coche

# Crear un objeto / instancia de la clase Coche
mi_coche = Coche()

print("Marca del coche:", mi_coche.marca)
print("Modelo del coche:", mi_coche.modelo)
print("Velocidad inicial:", mi_coche.get_velocidad())
mi_coche.acelerar()
print("Velocidad después de acelerar:", mi_coche.get_velocidad())
mi_coche.frenar()
print("Velocidad después de frenar:", mi_coche.get_velocidad())
