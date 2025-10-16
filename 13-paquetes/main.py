print('PROBANDO PAQUETES')
'''
from mipaquete import herramientas, pruebas # Importando el paquete completo
from mipaquete import pruebas # Importando un módulo concreto
from mipaquete.herramientas import nombreCompleto # Importando una función concreta
from mipaquete.pruebas import probando_paquete # Importando una función concreta
from mipaquete import * # Importando todo el paquete
from mipaquete.herramientas import * # Importando todo el módulo
from mipaquete.pruebas import * # Importando todo el módulo
'''
from mipaquete import pruebas, herramientas

print(herramientas.nombreCompleto("Juan", "Pérez"))
pruebas.probando_paquete()
