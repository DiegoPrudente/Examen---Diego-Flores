import math

class CalculadoraAreas:
    def calcular_area_circulo(self):
        try:
            radio = float(input("Introduce el radio del círculo: "))
            if radio < 0:
                print("El radio no puede ser negativo.")
                return
            area = math.pi * (radio ** 2)
            self.mostrar_resultado("Círculo", area)
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

    def calcular_area_triangulo(self):
        try:
            base = float(input("Introduce la base del triángulo: "))
            altura = float(input("Introduce la altura del triángulo: "))
            if base < 0 or altura < 0:
                print("La base y la altura no pueden ser negativas.")
                return
            area = 0.5 * base * altura
            self.mostrar_resultado("Triángulo", area)
        except ValueError:
            print("Entrada no válida. Por favor, introduce números.")

    def calcular_area_rectangulo(self):
        try:
            ancho = float(input("Introduce el ancho del rectángulo: "))
            alto = float(input("Introduce el alto del rectángulo: "))
            if ancho < 0 or alto < 0:
                print("El ancho y el alto no pueden ser negativos.")
                return
            area = ancho * alto
            self.mostrar_resultado("Rectángulo", area)
        except ValueError:
            print("Entrada no válida. Por favor, introduce números.")

    def mostrar_resultado(self, figura, area):
        print(f"El área del {figura} es: {area:.2f}")