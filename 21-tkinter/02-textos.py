from tkinter import *

ventana = Tk()
ventana.geometry("800x600")
texto = Label(ventana, text="¡Hola, bienvenido a Tkinter!")
texto.config(
    fg="white",
    bg="blue",
    font=("Arial", 12),
    padx=20,
    pady=20
)
texto.pack()

texto2 = Label(ventana, text="Esta es mi primera ventana.")
texto2.config(
    height=5,
    width=30,
    fg="yellow",
    bg="red",
    font=("Consolas", 12),
    padx=20,
    pady=20,
    cursor="heart"
)
texto2.pack(anchor=W)

def pruebas(nombre, apellidos, pais):
    return f"Hola, {nombre} {apellidos}, veo que eres de {pais}"

# Llamada a la función con argumentos nombrados (keyword arguments)
texto3 = Label(ventana, text=pruebas(apellidos="Pérez", nombre="Juan",  pais="España")) 
texto3.config(
    height=5,
    width=50,
    fg="green",
    bg="black",
    font=("Terminal", 14, "bold"),
    padx=20,
    pady=20,
    cursor="hand2"
)
texto3.pack(anchor=CENTER)

ventana.mainloop()