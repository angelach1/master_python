import notas.nota as modelo # Importar el módulo de nota.py como modelo


class Acciones:
    def crear(self, usuario):
        print(f'\nOK {usuario[1]}, vamos a crear una nota...')

        titulo = input('Introduce el título de la nota: ')
        descripcion = input('Introduce el contenido de la nota: ')

        nota = modelo.Nota(usuario[0], titulo, descripcion) # Crear instancia de Nota
        guardar = nota.guardar() # Llamar al método guardar

        if guardar[0] >= 1:
            print(f'\nPerfecto {usuario[1]}, has creado la nota: {nota.titulo}')
        else:
            print(f'\nNo se ha podido crear la nota {usuario[1]}!!')

    def mostrar(self, usuario):
        print(f'\nVale {usuario[1]}, aquí están tus notas...')

        nota = modelo.Nota(usuario[0]) # Crear instancia de Nota
        nota.mostrar() # Llamar al método mostrar

    def eliminar(self, usuario):
        print(f'\nOK {usuario[1]}, vamos a eliminar una nota...')

        titulo = input('Introduce el título de la nota a eliminar: ')

        #nota = modelo.Nota(usuario[0]) # Crear instancia de Nota
        nota = modelo.Nota(usuario[0], titulo) # Crear instancia de Nota
        nota.eliminar() # Llamar al método eliminar

