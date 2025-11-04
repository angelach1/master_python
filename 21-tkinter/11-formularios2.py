from tkinter import *

ventana = Tk()
ventana.title("Formularios con Tkinter - 2ª parte")
ventana.geometry("800x600")

encabezado = Label(ventana, text="Formularios 2ª parte")
encabezado.config(
    fg="white",
    bg="green", 
    padx=15, 
    pady=15, 
    font=("Consolas", 20))
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

def mostrarProfesion():
    texto = ""
    if web.get():
        texto += "Desarrollo web "
    if software.get():
        texto += "Desarrollo de software "
    if moviles.get():
        texto += "Desarrollo de aplicaciones móviles "
    mostrar.config(
        text="Te dedicas a: " + texto,
        fg="blue",
        font=("Consolas", 14)
    )

web = BooleanVar() # Variable para el checkbutton
software = BooleanVar() 
moviles = BooleanVar()

# Botones checkbutton (casillas de verificación)
Label(ventana, text="¿A qué te dedicas?").grid(row=1, column=0, sticky=W)
Checkbutton(
    ventana,
    text="Desarrollo web", 
    variable=web,
    onvalue=True,
    offvalue=False,
    command=mostrarProfesion
    ).grid(row=2, column=0, sticky=W)
Checkbutton(
    ventana,
    text="Desarrollo de software",
    variable=software,
    onvalue=True,
    offvalue=False,
    command=mostrarProfesion
).grid(row=3, column=0, sticky=W)
Checkbutton(
    ventana,
    text="Desarrollo de aplicaciones móviles",
    variable=moviles,
    onvalue=True,
    offvalue=False,
    command=mostrarProfesion
).grid(row=4, column=0, sticky=W)

mostrar = Label(ventana)
mostrar.grid(row=5, column=0, sticky=W)


# Botones de opción (radiobuttons)
opcion = IntVar() # Variable para los radiobuttons
#opcion.set(1) # Valor por defecto
opcion.set(NONE) # Sin valor por defecto

def mostrarOpcion():
    if opcion.get() == 1:
        marcado.config(text="Has seleccionado Python")
    elif opcion.get() == 2:
        marcado.config(text="Has seleccionado Java")
    elif opcion.get() == 3:
        marcado.config(text="Has seleccionado JavaScript")

Label(ventana, text="Selecciona tu lenguaje principal:").grid(row=8, column=0, sticky=W)
Radiobutton(
    ventana,
    text="Python", 
    variable=opcion,
    value=1,
    command=mostrarOpcion
).grid(row=8, column=1, sticky=W)
Radiobutton(
    ventana, 
    text="Java", 
    variable=opcion,
    value=2,
    command=mostrarOpcion
    ).grid(row=8, column=2, sticky=W)
Radiobutton(
    ventana,
    text="JavaScript",
    variable=opcion,
    value=3,
    command=mostrarOpcion
).grid(row=8, column=3, sticky=W)

marcado = Label(ventana)
marcado.grid(row=9, column=0, sticky=W)

# Menú de opciones (combobox)
Label(ventana, text="Selecciona una opción:").grid(row=11, column=0, sticky=W)
opcion = StringVar()
opcion.set("Opción 1") # Valor por defecto


select = OptionMenu(
    ventana,
    opcion,
    "Opción 1",
    "Opción 2",
    "Opción 3",
    "Opción 4"
)
select.grid(row=11, column=1, sticky=W)

def mostrarOpcionSeleccionada():
    seleccionado.config(
        text="Has seleccionado: " + opcion.get(),
        fg="purple",
        font=("Consolas", 14)
    )

boton = Button(ventana, text="Mostrar selección", command=mostrarOpcionSeleccionada)
boton.grid(row=12, column=0, sticky=W)

# Etiqueta para mostrar la opción seleccionada
seleccionado = Label(ventana)
seleccionado.grid(row=13, column=0, sticky=W)

# Iniciar el bucle principal de la ventana
ventana.mainloop()