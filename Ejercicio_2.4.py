import math

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado


class Triangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        h = self.hipotenusa()
        return self.base + self.altura + h

    def tipo(self):
        h = self.hipotenusa()

        if self.base == self.altura == h:
            return "Equilátero"
        elif self.base == self.altura or self.base == h or self.altura == h:
            return "Isósceles"
        else:
            return "Escaleno"


class Rombo:

    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    def area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def perimetro(self):
        return 4 * self.lado


class Trapecio:

    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def perimetro(self):
        return (self.base_mayor + self.base_menor +
                self.lado1 + self.lado2)


circulo = Circulo(5)
rectangulo = Rectangulo(10, 5)
cuadrado = Cuadrado(4)
triangulo = Triangulo(3, 4)
rombo = Rombo(10, 6, 5)
trapecio = Trapecio(10, 6, 4, 5, 5)

print("CÍRCULO")
print("Área:", circulo.area())
print("Perímetro:", circulo.perimetro())

print("\nRECTÁNGULO")
print("Área:", rectangulo.area())
print("Perímetro:", rectangulo.perimetro())

print("\nCUADRADO")
print("Área:", cuadrado.area())
print("Perímetro:", cuadrado.perimetro())

print("\nTRIÁNGULO")
print("Área:", triangulo.area())
print("Perímetro:", triangulo.perimetro())
print("Hipotenusa:", triangulo.hipotenusa())
print("Tipo:", triangulo.tipo())

print("\nROMBO")
print("Área:", rombo.area())
print("Perímetro:", rombo.perimetro())

print("\nTRAPECIO")
print("Área:", trapecio.area())
print("Perímetro:", trapecio.perimetro())