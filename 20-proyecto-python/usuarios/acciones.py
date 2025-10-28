class Acciones:
    def registro(self):
        print('\nOK!! Vamos a registrate en el sistema...')

        nombre = input('¿Cuál es tu nombre?: ')
        apellidos = input('¿Cuáles son tus apellidos?: ')
        email = input('¿Cuál es tu email?: ')
        password = input('¿Cuál es tu contraseña?: ')

        print(f'\nPerfecto {nombre}, ya estás registrado en el sistema!!')

    def login(self):
        print('\nPerfecto, identifícate en el sistema...')

        email = input('¿Cuál es tu email?: ')
        password = input('¿Cuál es tu contraseña?: ')

        print(f'\nBienvenido de nuevo {email}!!')