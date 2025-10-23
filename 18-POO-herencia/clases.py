# Herencia en Python. Es la capacidad de una clase de heredar atributos y métodos de otra clase.
# La clase que hereda se llama clase hija o subclase, y la clase de la que se hereda se llama clase padre o superclase.

class Persona:
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.altura = 0.0
        self.edad = 0

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellidos(self):
        return self.apellidos
    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def getAltura(self):
        return self.altura  
    def setAltura(self, altura):
        self.altura = altura

    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"
    def caminar(self):
        return "Estoy caminando"
    def dormir(self):
        return "Estoy durmiendo"
    # Fin de la clase Persona

class Informatico(Persona):  # La clase Informatico hereda de la clase Persona

    def __init__(self):
        self.lenguajes = "HTML, CSS, JS, PHP"
        self.experiencia = 5  # años de experiencia

    def getLenguajes(self):
        return self.lenguajes
    def setLenguajes(self, lenguajes):
        self.lenguajes = lenguajes

    def getExperiencia(self):
        return self.experiencia
    def setExperiencia(self, experiencia):
        self.experiencia = experiencia

    def programar(self):
        return "Estoy programando"
    def repararPC(self):
        return "He reparado el PC"
    def hacerWeb(self):
        return "Estoy haciendo una página web"
    # Fin de la clase Informatico

class TecnicoRedes(Informatico):  # La clase TecnicoRedes hereda de la clase Informatico
    
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase padre (Informatico) para inicializar sus atributos
        self.auditar = "Auditorías de seguridad"
        self.experienciaRedes = 3  # años de experiencia en redes

    def getAuditar(self):
        return self.auditar
    def setAuditar(self, auditar):
        self.auditar = auditar

    def getExperienciaRedes(self):
        return self.experienciaRedes
    def setExperienciaRedes(self, experienciaRedes):
        self.experienciaRedes = experienciaRedes

    def auditarRedes(self):
        return "Estoy auditando una red"
    def configurarRouter(self):
        return "Router configurado"
    # Fin de la clase TecnicoRedes






