import usuarios.usuario as modelo # Importar el módulo usuario.py como modelo
import notas.acciones as acciones_notas # Importar el módulo de acciones de notas

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
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e), e)
            print(type(e).__name__)
            print('\nLogin incorrecto!!')

    def proximasAcciones(self, login):
        print(f'''
              Acciones disponibles:
              - 1. Crear nota (crear)
              - 2. Mostrar notas (mostrar)
              - 3. Eliminar nota (eliminar)
              - 4. Salir (salir)
        ''')  
        accion = input('¿Qué quieres hacer?: ')
        hazEl = acciones_notas.Acciones() # Crear instancia de Acciones de notas        

        if accion == 'crear':

            print('Vamos a crear una nota!!')
            hazEl.crear(login)
            self.proximasAcciones(login) # Llamar de nuevo a proximasAcciones

        elif accion == 'mostrar':

            print('Aquí tienes tus notas!!')
            hazEl.mostrar(login)
            self.proximasAcciones(login)

        elif accion == 'eliminar':

            print('Vamos a eliminar una nota!!')
            hazEl.eliminar(login)
            self.proximasAcciones(login)
        elif accion == 'salir':
            print(f'\nHasta pronto {login[1]}!!')
            exit() #
        else:
            print('Esa acción no es correcta!!')
            self.proximasAcciones(login)

        return None
       