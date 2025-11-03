# Ejemplo de cómo mostrar imágenes en Tkinter usando Pillow

from tkinter import *
from PIL import ImageTk, Image # Asegúrate de tener Pillow instalado: pip install Pillow


ventana = Tk()
ventana.geometry("800x600")


Label(ventana,
      text="Imagen PNG en Tkinter",
      bg="white").pack(anchor=W)

imagen = Image.open("21-tkinter/imagenes/lobo.jpg")
render = ImageTk.PhotoImage(imagen)

Label(ventana,
      image=render,
      bg="white").pack(anchor=CENTER)

ventana.mainloop()