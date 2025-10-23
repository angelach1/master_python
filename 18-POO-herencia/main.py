import clases

persona = clases.Persona()
persona.setNombre("Juan")
persona.setApellidos("Pérez")
persona.setAltura(1.75)
persona.setEdad(30)

print(f"La persona se llama {persona.getNombre()} {persona.getApellidos()}, mide {persona.getAltura()} metros y tiene {persona.getEdad()} años.")
print(persona.hablar())
print(persona.caminar())
print(persona.dormir())
print("\n---\n")

informatico = clases.Informatico()
informatico.setNombre("Ana")
informatico.setApellidos("García")
informatico.setAltura(1.65)
informatico.setEdad(28)
informatico.setLenguajes("Python, Java, C++")
informatico.setExperiencia(6)
print(f"El informático se llama {informatico.getNombre()} {informatico.getApellidos()}, mide {informatico.getAltura()} metros y tiene {informatico.getEdad()} años.")
print(f"Lenguajes: {informatico.getLenguajes()}")
print(f"Años de experiencia: {informatico.getExperiencia()}")
print(informatico.hablar())
print(informatico.programar())
print(informatico.repararPC())
print(informatico.hacerWeb())

print("\n---\n")
print("Comprobando herencia:")
print(informatico.caminar())  # Método heredado de la clase Persona
print(informatico.dormir())    # Método heredado de la clase Persona

print("\n---\n")
tecnico = clases.TecnicoRedes() # La clase TecnicoRedes hereda de la clase Informatico
tecnico.setNombre("Luis") # Establecer nombre usando método heredado
print(f"El técnico de redes se llama {tecnico.getNombre()}") # Obtener nombre usando método heredado
print(tecnico.auditarRedes()) # Método propio de la clase TecnicoRedes




