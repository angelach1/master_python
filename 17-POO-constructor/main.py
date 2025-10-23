from coche import Coche

# Crear un objeto / instancia de la clase coche
coche1 = Coche("Rojo", "Ferrari", "Aventador", 300, 500, 2) # Pasar los parámetros al constructor
coche2 = Coche("Azul", "Toyota", "Corolla", 180, 140, 5)   # Pasar los parámetros al constructor
coche3 = Coche("Verde", "Tesla", "Model S", 250, 400, 5)   # Pasar los parámetros al constructor


print("Coche 1:")
print("Color:", coche1.getColor())
print("Marca:", coche1.getMarca())
print("Modelo:", coche1.getModelo())
print("Velocidad:", coche1.get_velocidad(), "km/h")
print()
print("Coche 2:")
print("Color:", coche2.getColor())
print("Marca:", coche2.getMarca())
print("Modelo:", coche2.getModelo())
print("Velocidad:", coche2.get_velocidad(), "km/h")
# Acelerar el coche1
coche1.acelerar()
print("\nDespués de acelerar el coche 1:")
print("Velocidad del coche 1:", coche1.get_velocidad(), "km/h")
# Frenar el coche2
coche2.frenar()
print("\nDespués de frenar el coche 2:")
print("Velocidad del coche 2:", coche2.get_velocidad(), "km/h")
print("\nInformación completa del coche 1:")
print(coche1.getInfo())
print("Información completa del coche 2:")
print(coche2.getInfo())
print("Información completa del coche 3:")
print(coche3.getInfo())

# Detectar el tipo de dato
print("\nTipo de dato de coche1:", type(coche1))

if type(coche1) == Coche:
    print("coche1 es una instancia de la clase Coche")  
else:
    print("coche1 no es una instancia de la clase Coche")

# hacer lo mismo pero con isinstance
if isinstance(coche2, Coche):
    print("coche2 es una instancia de la clase Coche")    
else:
    print("coche2 no es una instancia de la clase Coche")   

# Visibilidad de atributos
print("\nAccediendo a un atributo público:", coche1.soy_publico)
# Intentar acceder a un atributo privado (esto generará un error)
# print("Accediendo a un atributo privado:", coche1.__soy_privado)  # Descomentar para ver el error
print("Accediendo a un atributo privado mediante un método getter:", coche1.getPrivado())



# Fin del programa

