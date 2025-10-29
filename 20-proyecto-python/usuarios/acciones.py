import usuarios.usuario as modelo # Importar el módulo usuario.py como modelo

class Acciones:
    def registro(self):
        print('\nOK!! Vamos a registrate en el sistema...')

        nombre = input('¿Cuál es tu nombre?: ')
        apellidos = input('¿Cuáles son tus apellidos?: ')
        email = input('¿Cuál es tu email?: ')
        password = input('¿Cuál es tu contraseña?: ')
        
        usuario = modelo.Usuario(nombre, apellidos, email, password) # Crear instancia de Usuario
        registro = usuario.registrar() # Llamar al método registrar

        if registro[0] >= 1:
            print(f'\nPerfecto {registro[1].nombre}, te has registrado con el email {registro[1].email}')
        else:
            print('\nNo te has registrado correctamente!!')

    def login(self):
        print('\nPerfecto, identifícate en el sistema...')

        email = input('¿Cuál es tu email?: ')
        password = input('¿Cuál es tu contraseña?: ')

        usuario = modelo.Usuario('','', email, password) # Crear instancia de Usuario
        login = usuario.identificar() # Llamar al método identificar
        
        try:
            if email == login[3]:
                print(f'\nBienvenido de nuevo {login[1]}, te has registrado el {login[5]}!!')
                self.proximasAcciones(usuario)
        except Exception as e:
            print(type(e), e)
            print(type(e).__name__)
            print('\nLogin incorrecto!!')

    def proximasAcciones(self, usuario):
        print(f'\nAcciones disponibles:\n  - Crear nota\n  - Mostrar notas\n  - Eliminar nota\n  - Salir')  

        return None
       