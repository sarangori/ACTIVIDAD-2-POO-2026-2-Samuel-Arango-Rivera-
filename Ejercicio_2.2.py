class Planeta:
    

    def __init__(self, nombre, cantidad_satelites, masa, volumen,
                 diametro, distancia_sol, tipo, observable, orbital, rotacion):

        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.observable = observable
        self.orbital = orbital
        self.rotacion = rotacion

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Satélites:", self.cantidad_satelites)
        print("Masa:", self.masa)
        print("Volumen:", self.volumen)
        print("Diámetro:", self.diametro)
        print("Distancia al Sol:", self.distancia_sol)
        print("Tipo:", self.tipo)
        print("Observable:", self.observable)
        print("Periodo orbital", self.orbital)
        print("Periodo de rotacion", self. rotacion)

    def calcular_densidad(self):
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        distancia_ua = self.distancia_sol / 149.59787
        return distancia_ua > 3.4

def main():

    planeta1 = Planeta(
        "Tierra", 1, 5.972e24, 1.083e12,
        12742, 149.6, "TERRESTRE", True, 365.25, 0.997
    )

    planeta2 = Planeta(
        "Jupiter", 95, 1.898e27, 1.431e15,
        139820, 778.5, "GASEOSO", True, 4333, 0.414 
    )

    planeta1.imprimir()
    print("Densidad:", planeta1.calcular_densidad())
    print("¿Es exterior?", planeta1.es_planeta_exterior())

    print()

    planeta2.imprimir()
    print("Densidad:", planeta2.calcular_densidad())
    print("¿Es exterior?", planeta2.es_planeta_exterior())


main()