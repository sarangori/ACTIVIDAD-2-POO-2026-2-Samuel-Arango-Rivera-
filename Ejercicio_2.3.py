class Automovil:

    def __init__(self, marca, modelo, motor, combustible, tipo,
                 puertas, asientos, velocidad_maxima, color, automatico):

        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.combustible = combustible
        self.tipo = tipo
        self.puertas = puertas
        self.asientos = asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0
        self.automatico = automatico
        self.multas = []

    
    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_motor(self):
        return self.motor

    def set_motor(self, motor):
        self.motor = motor

    def get_combustible(self):
        return self.combustible

    def set_combustible(self, combustible):
        self.combustible = combustible

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_puertas(self):
        return self.puertas

    def set_puertas(self, puertas):
        self.puertas = puertas

    def get_asientos(self):
        return self.asientos

    def set_asientos(self, asientos):
        self.asientos = asientos

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_automatico(self):
        return self.automatico

    def set_automatico(self, automatico):
        self.automatico = automatico

    
    def acelerar(self, velocidad):
        self.velocidad_actual += velocidad

        if self.velocidad_actual > self.velocidad_maxima:
            exceso = self.velocidad_actual - self.velocidad_maxima
            multa = exceso * 10
            self.multas.append(multa)
            print("¡Se generó una multa de:", multa)

        print("Velocidad actual:", self.velocidad_actual, "km/h")

    
    def desacelerar(self, velocidad):
        self.velocidad_actual -= velocidad
        print("Velocidad actual:", self.velocidad_actual, "km/h")

    
    def frenar(self):
        self.velocidad_actual = 0
        print("Velocidad actual:", self.velocidad_actual, "km/h")

    
    def tiempo_llegada(self, distancia):
        if self.velocidad_actual == 0:
            return 0

        return distancia / self.velocidad_actual

    
    def mostrar(self):
        print("\n--- AUTOMÓVIL ---")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Motor:", self.motor, "L")
        print("Combustible:", self.combustible)
        print("Tipo:", self.tipo)
        print("Puertas:", self.puertas)
        print("Asientos:", self.asientos)
        print("Velocidad máxima:", self.velocidad_maxima)
        print("Color:", self.color)
        print("Velocidad actual:", self.velocidad_actual)
        print("Automático:", self.automatico)

    
    def tiene_multas(self):
        return len(self.multas) > 0

    
    def total_multas(self):
        return sum(self.multas)

auto = Automovil(
    "Toyota",
    2025,
    2.0,
    "gasolina",
    "SUV",
    5,
    5,
    200,
    "rojo",
    True
)

auto.mostrar()

auto.acelerar(100)

auto.acelerar(20)

auto.desacelerar(50)

print("Tiempo de llegada:", auto.tiempo_llegada(200), "horas")

auto.acelerar(200)

print("¿Tiene multas?", auto.tiene_multas())
print("Total de multas:", auto.total_multas())

auto.frenar()