# Tkinter
# Módulo estándar de Python para crear interfaces gráficas de usuario (GUI)

from tkinter import *
import os.path # Módulo para operaciones del sistema operativo

class Programa:
    def __init__(self):
       self.title = "Mi primera ventana con Tkinter"
       self.icon = "/imagenes/logotipo.ico"
       self.icon_alt = "/21-tkinter/imagenes/logotipo.ico"
       self.size = "800x600"
       self.resizable = False

    def cargar(self):
        
        # Crear la ventana principal
        self.ventana = Tk()

        # Al ejecutar este código, se abrirá una ventana vacía creada con Tkinter.
        # La ventana permanecerá abierta hasta que el usuario la cierre manualmente.
        # Nota: Asegúrate de tener Python instalado en tu sistema para ejecutar este código.

        # Comprobar si existe un archivo de icono
        ruta_icono = str(os.path.abspath(os.path.dirname(__file__))) + self.icon
        if not os.path.isfile(ruta_icono):
            ruta_icono = str(os.path.abspath(os.path.dirname(__file__))) + self.icon_alt

        # Mostrar texto en la ventana
        texto = Label(self.ventana, text=ruta_icono)
        texto.pack()

        # Icono de la ventana
        self.ventana.iconbitmap(ruta_icono)  # Cambia el icono de la ventana (asegúrate de tener el archivo icono.ico en el mismo directorio)

        # Título de la ventana
        self.ventana.title(self.title)  # Establece el título de la ventana

        self.ventana.geometry(self.size)  # Establece el tamaño de la ventana a 800x600 píxeles

        # Bloquear el cambio de tamaño de la ventana
        if self.resizable :
            self.ventana.resizable(1, 1)  # La ventana se puede redimensionar tanto en ancho como en alto
        else:
            self.ventana.resizable(0, 0)  # La ventana no se puede redimensionar

    def addTexto(self, texto):
        etiqueta = Label(self.ventana, text=texto)
        etiqueta.pack()
        
    # Arrancar y mostrar la ventana hasta que se cierre
    # Este método debe llamarse al final del programa para mantener la ventana abierta
    def mostrar(self):   
        self.ventana.mainloop() # Mantiene la ventana abierta y espera a que el usuario la cierre


    # Fin clase Programa

# Crear una instancia de la clase Programa y cargar la ventana
mi_programa = Programa()
mi_programa.cargar() # Cargar la ventana con las configuraciones iniciales
mi_programa.addTexto("¡Hola, bienvenido a Tkinter!")
mi_programa.addTexto("Esta es mi primera ventana.")
mi_programa.addTexto("Estoy aprendiendo a usar Tkinter con Python.")
mi_programa.mostrar() # Mostrar la ventana y esperar a que se cierre
