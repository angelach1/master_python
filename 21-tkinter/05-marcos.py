# Ejemplo de uso de marcos (Frames) en Tkinter

from tkinter import *

ventana = Tk()
ventana.title("Ejemplo de Marcos en Tkinter")
ventana.geometry("800x600")

marco_padre = Frame(ventana, width=780, height=580, bg="lightgray", bd=10) #
marco_padre.pack(padx=10, pady=10)

marco1 = Frame(marco_padre,width=250, height=250, bg="blue", bd=25) # Marco hijo dentro del marco padre
marco1.config(
    bg="red",
    bd=5,
    relief="groove",
    cursor="hand2"
)
marco1.pack(side=RIGHT, anchor=NE, padx=10, pady=10) # Posicionado en la esquina superior derecha
marco1.pack_propagate(False) # Evita que el marco se ajuste al tamaño del contenido

texto = Label(marco1, text="Primer marco")
texto.config(
    fg="white",
    bg="red",
    font=("Arial", 16),
    anchor=CENTER,
    height=4,
    width=10,
    bd=3,
    relief="raised",
    cursor="heart"
)
texto.pack()

marco2 = Frame(marco_padre,width=250, height=250, bg="green", bd=25) # Marco hijo dentro del marco padre
marco2.config(
    bg="green",
    bd=25,
    relief="sunken",
    cursor="hand2"
)
marco2.pack(side=LEFT, anchor=NW, padx=10, pady=10) # Posicionado en la esquina superior izquierda

marco3 = Frame(ventana,width=250, height=250, bg="green", bd=25)
marco3.config(
    bg="blue",
    bd=25,
    relief="sunken",
    cursor="hand2"
)
marco3.pack(side=RIGHT, anchor=NE, padx=10, pady=10) # Posicionado en la esquina superior derecha

ventana.mainloop()