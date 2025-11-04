# Ejemplo de menú en Tkinter
from tkinter import *

ventana = Tk()

# Crear un menú
mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

# Crear un submenú
submenu_archivo = Menu(mi_menu, tearoff=0) # tearoff=0 elimina la línea punteada al inicio
mi_menu.add_cascade(label="Archivo", menu=submenu_archivo)
submenu_archivo.add_command(label="Nuevo")
submenu_archivo.add_command(label="Abrir")
submenu_archivo.add_separator()
submenu_archivo.add_command(label="Salir", command=ventana.quit)
submenu_editar = Menu(mi_menu, tearoff=0)
mi_menu.add_cascade(label="Editar", menu=submenu_editar)
submenu_editar.add_command(label="Cortar")
submenu_editar.add_command(label="Copiar")
submenu_editar.add_command(label="Pegar")
submenu_editar.add_separator()
submenu_editar.add_command(label="Deshacer")
submenu_editar.add_command(label="Rehacer")
submenu_ayuda = Menu(mi_menu, tearoff=0)
mi_menu.add_cascade(label="Ayuda", menu=submenu_ayuda)
submenu_ayuda.add_command(label="Acerca de")
submenu_ayuda.add_command(label="Documentación")


# Ejecutar la ventana
ventana.mainloop()