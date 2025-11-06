"""
Crear un programa que tenga:
- ventana con un título y un tamaño específico.
- No redimensionable.
- Un menú (Inicio, Añadir, Información, Salir)
- Diferentes pantallas
- Formulario para añadir productos
- Guardar los datos temporales en una lista
- Mostrar los datos listados en la pantalla principal
- Opción de salir del programa desde el menú

"""

from tkinter import *
from tkinter import ttk # Importar ttk para usar widgets mejorados

# Configuración de la ventana principal
ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(500, 500) # Tamaño mínimo de la ventana, la cual se expandirá según el contenido
ventana.title("Proyecto Tkinter - Master en Python")
ventana.resizable(0, 0)

# Pantallas
def home():
    # Mostrar encabezado
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=100,
        pady=20
    )
    home_label.grid(row=0, column=0,)

    # Mostrar productos añadidos
    products_box.grid(row=2, column=0, padx=20, pady=20)

    """
    for product in products:
        if len(product) == 3:
            product.append("added")  # Marcar como añadido para evitar duplicados

            product_frame = Frame(products_box, bd=2, relief="groove", padx=10, pady=10)
            product_frame.pack(fill="x", pady=5)

            name_label = Label(product_frame, text=f"Nombre: {product[0]}", font=("Arial", 12, "bold"))
            name_label.pack(anchor="w")

            price_label = Label(product_frame, text=f"Precio: {product[1]}", font=("Arial", 12))
            price_label.pack(anchor="w")

            description_label = Label(product_frame, text=f"Descripción: {product[2]}", font=("Arial", 12), wraplength=400, justify="left")
            description_label.pack(anchor="w")
    """
    for product in products:
        if len(product) == 3:
            product.append("added")  # Marcar como añadido para evitar duplicados
            products_box.insert("", 0, text=product[0], values=(product[1], product[2]))
    
    # Ocultar otras pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add():
    # Mostrar Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=110,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10) # Encabezado ocupa diez columnas

    # Campos de la pantalla de añadir productos
    # Contenedor de los campos
    add_frame.grid(row=1, column=0, columnspan=10, padx=20, pady=20)

    # Campo de nombre del producto alineado a la izquierda
    add_name_label.grid(row=1, column=0, sticky="nw", padx=10, pady=5) # Ajuste para que la etiqueta no ocupe todo el ancho
    add_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w") # Ajuste para que la entrada no ocupe todo el ancho

    # Campo de precio del producto alineado a la izquierda
    add_price_label.grid(row=2, column=0, sticky="nw", padx=10, pady=5) 
    add_price_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    # Campo de descripción del producto alineado a la izquierda
    add_description_label.grid(row=3, column=0, sticky="nw", padx=10, pady=5)
    add_description_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    # Botón de guardar
    boton_guardar.grid(row=4, column=1, padx=10, pady=20, sticky="nw")
    boton_guardar.config(
        width=10,
        padx=10,
        pady=5,
        bg="green",
        fg="white",
        font=("Arial", 12)
        )

    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
        )

    # Ocultar otras pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=160,
        pady=20
    )
    info_label.grid(row=0, column=0)

    # Ocultar otras pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()

    data_label.grid(row=1, column=0)
    return True

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")  

    ])
    # Limpiar los campos después de guardar
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    # print(products) # Para verificar que se guardan los productos correctamente viendolo en la consola

    home() # Volver a la pantalla de inicio después de guardar
    return True
        
# Variables globales 
products = [] # Lista para almacenar productos temporalmente
name_data = StringVar()
price_data = StringVar()

# Definir campos de pantallas para que sean variables globales
# Definir la etiqueta de la pantalla de inicio
home_label = Label(ventana, text="Pantalla de Inicio", font=("Arial", 24))
#products_box = Frame(ventana, width=250)
Label(ventana).grid(row=1) # Espaciador entre el encabezado y la tabla

products_box = ttk.Treeview(height=12, columns=2) # Tabla para mostrar productos
products_box.grid(row=2, column=0, columnspan=2)
products_box.heading("#0", text="Nombre", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)



# Definir campos de la pantalla de añadir productos
add_label = Label(ventana, text="Añadir Producto", font=("Arial", 24))

# Definir campos de la pantalla de añadir productos
add_frame = Frame(ventana) # Contenedor de los campos

add_name_label = Label(add_frame, text="Nombre:")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio:")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción:")
add_description_entry = Text(add_frame, height=5, width=30)

boton_guardar = Button(add_frame, text="Guardar", command=add_product)

# Definir campos de la pantalla de información
info_label = Label(ventana, text="Información", font=("Arial", 24))
data_label = Label(ventana, text="Proyecto realizado por Ángel Alhambra - 2025", font=("Arial", 12))



# Cargar pantalla de inicio por defecto
home()

# Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# Configurar el menú en la ventana
ventana.config(menu=menu_superior)



# Iniciar el bucle principal de la ventana
ventana.mainloop()