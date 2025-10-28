'''
Proyecto Python - MysqlL
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la base de datos
- Si elegimos login, identificará al usuario y nos breguntará por una serie de opciones:
    - Crear nota
    - Mostrar notas
    - Eliminar nota
    - Salir
'''
from usuarios import acciones #Importar el módulo acciones del paquete usuarios


print('''
Acciones disponibles:
      - registro
      - login

''')

hazEl = acciones.Acciones() #Crear instancia de la clase Acciones
accion = input('¿Qué deseas hacer?: ')

if accion == 'registro':
    hazEl.registro()
    
elif accion == 'login':
    hazEl.login()


    
    