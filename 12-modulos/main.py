'''
Módulos: Son funcionalidades ya hechas que podemos importar a nuestros proyectos para no tener que programarlas desde cero.

Existen módulos nativos de Python y módulos externos que podemos instalar con pip.
También podemos crear nuestros propios módulos.

Para importar un módulo usamos la palabra reservada import seguida del nombre del módulo.
'''

# Importar módulo propio
import mimodulo # Importa todo el módulo y se accede con mimodulo.funcion()
from mimodulo import saludar, calculadora # Importa funciones específicas y se accede directamente por su nombre
from mimodulo import * # Importa todo el módulo y se accede directamente por su nombre

# Usar funciones del módulo
print(mimodulo.saludar("Juan"))
print(saludar("María"))
print(calculadora(10, 5, "sumar"))
print(calculadora(10, 5, "restar"))
print(calculadora(10, 5, "multiplicar"))
print(calculadora(10, 5, "dividir"))

# Módulo de fechas
import datetime

fecha_actual = datetime.datetime.now()
print(fecha_actual)
print(fecha_actual.year)
print(fecha_actual.month)
print(fecha_actual.day)
print(fecha_actual.hour)

# Formatear fecha
print(fecha_actual.strftime("%d/%m/%Y"))
print(fecha_actual.strftime("%B %d, %Y, %H:%M:%S"))
print(fecha_actual.strftime("Hoy es %A, %d de %B de %Y"))

# Módulo matemáticas
import math
print(f'El número PI es: {math.pi}')
print(f'La raíz cuadrada de 16 es: {math.sqrt(16)}')
print(f'El factorial de 5 es: {math.factorial(5)}')
print(f'2 elevado a la 3 es: {math.pow(2, 3)}')
print(f'El valor absoluto de -7 es: {math.fabs(-7)}')
# Redondear números
print(f'El redondeo de 4.6 es: {math.ceil(4.6)}')
print(f'El redondeo de 4.4 es: {math.floor(4.4)}')

# Módulo random
import random
print(f'Número aleatorio entre 1 y 10: {random.randint(1, 10)}')
print(f'Número aleatorio entre 0 y 1: {random.random()}')
print(f'Número aleatorio entre 0 y 100: {random.uniform(0, 100)}')
print(f'Elemento aleatorio de una lista: {random.choice(["rojo", "verde", "azul"])}')


