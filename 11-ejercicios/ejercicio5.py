'''
Ejercicio 5: Crear una lista con el contenido de esta tabla de videojuegos:

| Título               | Año  | Género         |
|----------------------|------|----------------|
| The Legend of Zelda  | 1986 | Aventura       |
| Super Mario Bros.    | 1985 | Plataformas    |
| Dark Souls           | 2011 | RPG            |
| Overwatch            | 2016 | Shooter        |
| Minecraft            | 2011 | Sandbox        |

Mostrar por pantalla el título, año y género de cada videojuego.
'''
videojuegos = [
    {"Título": "The Legend of Zelda", "Año": 1986, "Género": "Aventura"},
    {"Título": "Super Mario Bros.", "Año": 1985, "Género": "Plataformas"},
    {"Título": "Dark Souls", "Año": 2011, "Género": "RPG"},
    {"Título": "Overwatch", "Año": 2016, "Género": "Shooter"},
    {"Título": "Minecraft", "Año": 2011, "Género": "Sandbox"},
]

for juego in videojuegos:
    print(f"Título: {juego['Título']}, Año: {juego['Año']}, Género: {juego['Género']}")

# Alternativamente, usando unpacking
print("\nUsando unpacking:")    
for juego in videojuegos:
    titulo, año, género = juego.values()
    print(f"Título: {titulo}, Año: {año}, Género: {género}")

# Otra forma usando f-strings directamente
print("\nUsando f-strings directamente:")
for juego in videojuegos:
    print(f"{juego['Título']} ({juego['Año']}) - Género: {juego['Género']}")

''' 
Ejercicio 6: Crear una lista con el contenido de esta tabla de videojuegos:
 ACCIÓN  | AVENTURA | RPG | SHOOTER | PLATAFORMAS | SANDBOX 
|--------|----------|-----|---------|-------------|---------|
| GTA    | Zelda    | Skyrim | Call of Duty | Mario| Minecraft |
| Witcher| Uncharted| Final Fantasy | Halo        | Sonic      | Terraria  |
| Doom   | Tomb Raider | Mass Effect | Battlefield | Donkey Kong | Roblox    |  

Mostrar esta información ordenada por género.

'''
tabla = [
    {
    'categoria':"ACCIÓN",
    'juegos': ["GTA", "Witcher", "Doom"]
    },
    {'categoria':"AVENTURA",
    'juegos': ["Zelda", "Uncharted", "Tomb Raider"]
    },
    {'categoria':"RPG",
    'juegos': ["Skyrim", "Final Fantasy", "Mass Effect"]
    },
    {'categoria':"SHOOTER",
    'juegos': ["Call of Duty", "Halo", "Battlefield"]
    },
    {'categoria':"PLATAFORMAS",
    'juegos': ["Mario", "Sonic", "Donkey Kong"]
    },
    {'categoria':"SANDBOX",
    'juegos': ["Minecraft", "Terraria", "Roblox"]
    }
]

for categoria in tabla:
    print(f"-----------------{categoria['categoria']}--------------")
    for juego in categoria['juegos']:
        print(f"- {juego}")