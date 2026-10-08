class Persona:
    
    def __init__(self, nombre, apellido, documento, a_nacimiento, p_nacimiento, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.a_nacimiento = a_nacimiento
        self.p_nacimiento = p_nacimiento
        self.genero = genero

    
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Documento:", self.documento)
        print("Año de nacimiento:", self.a_nacimiento)
        print("País de nacimiento:", self.p_nacimiento)
        print("Género:", self.genero)



def main():
    
    persona1 = Persona("Samuel", "Arango", "123456789", 2008, "Colombia", "H")
    persona2 = Persona("Juan", "Perez", "987654321", 1536, "Perú","H")

    print("PERSONA 1")
    persona1.imprimir()

    print("\nPERSONA 2")
    persona2.imprimir()

main()