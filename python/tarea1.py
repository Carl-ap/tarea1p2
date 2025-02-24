import math
import matplotlib.pyplot as plt
import numpy as np

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        radio = math.sqrt(self.x * self.x + self.y * self.y)
        angulo = math.atan2(self.y, self.x)
        angulo = math.degrees(angulo)
        return radio, angulo     

    def __str__(self):
        return "({:.2f},{:.2f})".format(self.x, self.y)
    
    
p1 = Punto(0, 3)
p2 = Punto(4, 0)
print(p1)
print(p2)
x1, y1 = p1.coord_cartesianas()
print(x1, y1)
r1, a1 = p1.coord_polares()
print(r1, a1)
x2, y2 = p2.coord_cartesianas()
print(x2, y2)
r2, a2 = p2.coord_polares()
print(r2, a2)

class Linea:
    def __init__(self, punto1, punto2):
        self.p1 = punto1
        self.p2 = punto2
    
    def DibujarLinea(self):
        x = [self.p1.x, self.p2.x]
        y = [self.p1.y, self.p2.y]
        plt.plot(x, y)
        
        # Añadir título y etiquetas
        plt.title("Gráfico de línea")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        
        # Mostrar el gráfico
        plt.show()

# Crear instancia de la clase Linea y dibujar la línea
linea = Linea(p1, p2)
linea.DibujarLinea()

class Circulo:
    def __init__(self, centro, radio):
        self.c = centro
        self.r = radio
    
    def DibujarCirculo(self):
        theta = np.linspace(0, 2 * np.pi, 100)

        # Calcular las coordenadas x e y del círculo
        x = self.c.x + self.r * np.cos(theta)
        y = self.c.y + self.r * np.sin(theta)

        # Crear la gráfica
        plt.plot(x, y)

        # Asegurarse de que los ejes tienen la misma escala
        plt.axis('equal')

        # Añadir título y etiquetas
        plt.title("Círculo")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")

        # Mostrar el gráfico
        plt.show()

# Crear instancia de la clase Circulo y dibujar el círculo
centro = Punto(2, 2)
circulo = Circulo(centro, 5)
circulo.DibujarCirculo()
