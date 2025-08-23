
# LUIS FERNANDO SEGOBIA TORRES 2177528
# A 20/08/2025
# ESTE PROGRAMA CALCULA LA CANTIDAD MINIMA DE MATERIAL
# PARA FABRICAR CILINDROS QUE CONTENGAN 1L DE CAPACIDAD

import os
import math

def cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

def format(num):
        return "------    " if num is None else f"{num:<10.8f}"

def print_registro(x_i, x_iPlus, error):
    print(f"{format(x_i)} | {format(x_iPlus)} | {format(error)}")

def f_plus(delta, x_i) -> float:
    return x_i - ((delta*f_x(x_i)) / (f_x(x_i + delta) - f_x(x_i)))

def f_x(x:float) -> float:
    return -2000/x**3 - 2000/x**2 + 4*math.pi*x + 2*math.pi

def f_error(x_i, x_iPlus) ->float:
    return abs((x_iPlus - x_i ) / x_iPlus)

class Raices:
    def __init__(self, delta, x_i, x_iPlus = None, error = 100):
        self.delta = delta
        self.x_i = x_i
        self.x_iPlus = x_iPlus
        self.error = error

    def print_table(self)->float:
        print('\n*****Tabla de resultados*****\n')
        print(f' {"x_i":<10} | {"x_i+1":<10} | {"error":<10}')
        for _ in range(50):
            print('-', end = '')
        print()
        while(self.error > 0.0001):
            self.x_iPlus = f_plus(self.delta, self.x_i)
            self.error = f_error(self.x_i, self.x_iPlus)
            print_registro(self.x_i, self.x_iPlus, self.error)
            self.x_i = self.x_iPlus
        return self.x_iPlus


cleaner()
print('***** SISTEMA PARA CALCULAR CANTIDAD MINIMA DE MATERIAL *****\n *** UTILIZADO PARA FABRICAR CILINDROS CON CAPACIDAD DE 1L ***')
print('Se utiliza el metodo de la secante modificada y se toma como x_0 = 6 y como delta = 0.01')
print("Siendo 1L de capacidad -> debe ser v = 1000 cm**3 = pi * x**2 * h, ademas tiene un borde de 0.5 cm -> area = 2*pi*h*(x+1/2)")
print('Entonces quedaria sustituyendo al ultimo como f(x) = (1000/x**2) * (2x+1) + 2*pi*(x+1/2)**2')
print("Como queremos obtener el valor minimo debemos encontrar los puntos criticos con f'(x) = -2000/x**3 - 2000/x**2 + 4*pi*x + 2*pi")

raiz_1 = Raices(0.01, 6)
res = raiz_1.print_table()
print(f"\nPor lo tanto el valor que mas se aproxima a el punto critico donde f'(x) = 0 con un error del 0.0001 es de {round(res, 5)}")

print("\nPrograma realizado por Luis Fernando Segobia Torres 2177528 a 20/08/2025")
