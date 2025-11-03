from tkinter import *

ventana = Tk()
ventana.geometry("800x600")
ventana.title("Formularios en Tkinter")

# Texto de encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - Angel Alhambra")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18, "bold"),
    padx=10,
    pady=10,
    bd=5
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W, padx=5, pady=5) # con columnspan abarca varias columnas

# Etiqueta para el campo de nombre
etiqueta_nombre = Label(ventana, text="Nombre:")
etiqueta_nombre.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Campo de entrada de texto
campo_nombre = Entry(ventana)
campo_nombre.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_nombre.config(
    fg="blue",
    font=("Arial", 12),
    justify="left",
    state=NORMAL
)

# Etiqueta para el campo Apellidos
etiqueta_apellidos = Label(ventana, text="Apellidos:")
etiqueta_apellidos.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Campo de entrada de texto
campo_apellidos = Entry(ventana)
campo_apellidos.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_apellidos.config(
    fg="blue",
    font=("Arial", 12),
    justify="left",
    state=NORMAL
)

# Etiqueta para el campo descripción
etiqueta_descripcion = Label(ventana, text="Descripción:")
etiqueta_descripcion.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Campo de entrada de texto
campo_descripcion = Text(ventana, height=5, width=40)
campo_descripcion.grid(row=3, column=1, sticky=W, padx=5, pady=5)
campo_descripcion.config(
    fg="blue",
    font=("Arial", 12),
    padx=15,
    pady=15,
    width=30,
    height=10,
    wrap=WORD
)

# Botón de envío
Label(ventana, text="").grid(row=4, column=0) # Espaciador

boton_enviar = Button(ventana, text="Enviar")
boton_enviar.grid(row=5, column=1, sticky=W, padx=5, pady=5)
boton_enviar.config(
    fg="white",
    bg="green",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10,
    cursor="hand2"
)

ventana.mainloop()