"""LUIS FERNANDO SEGOBIA TORRES 2177528
A 17/08/2025
ESTE PROGRAMA CALCULA UNA RAIZ REAL CON EL METODO
DE PUNTO FIJO"""

import os
import math

def cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

def format(num):
        return "------    " if num is None else f"{num:<10.8f}"

def print_registro(x_iLess, x_i, x_iPlus, error):
    print(f"{format(x_iLess)} | {format(x_i)} | {format(x_iPlus)} | {format(error)}")

def f_plus(x_iLess, x_i) -> float:
    return x_i - (f_x(x_i)*(x_iLess - x_i)/(f_x(x_iLess) - f_x(x_i)))

def f_x(x:float) -> float:
    return math.exp(x) - math.pi * x

def f_error(x_i, x_iPlus) ->float:
    return abs((x_iPlus - x_i ) / x_iPlus)

class Raices:
    def __init__(self, x_iLess, x_i, x_iPlus, error = 100):
        self.x_iLess = x_iLess
        self.x_i = x_i
        self.x_iPlus = x_iPlus
        self.error = error

    def print_table(self)->float:
        print('\n*****Tabla de resultados*****\n')
        print(f'{"x_i-1":<10} | {"x_i":<10} | {"x_i+1":<10} | {"error":<10}')
        for _ in range(50):
            print('-', end = '')
        print()
        while(self.error > 0.000001):
            self.x_iPlus = f_plus(self.x_iLess, self.x_i)
            self.error = f_error(self.x_i, self.x_iPlus)
            print_registro(self.x_iLess, self.x_i, self.x_iPlus, self.error)
            self.x_iLess = self.x_i
            self.x_i = self.x_iPlus
        return self.x_iPlus


cleaner()
print('\n*******METODO DE LA SECANTE********\n*******CALCULA RAICES REALES********\n')
print("Siendo f(x) = e**x - pi*x una funcion continua, se obtendran las raices aproximadas con un error del 0.000001")

# Para la primer raiz tendremos como x_0 = 0.5 y x_1 = 0.75
raiz_1 = Raices(0.5, 0.75, None)
res = raiz_1.print_table()
print(f"\nPor lo tanto el valor que mas se aproxima a la primer raiz con un error del 0.000001 es de {round(res, 5)}")

# Para la primer raiz tendremos como x_0 = 1.5 y x_1 = 1.75
raiz_2 = Raices(1.5, 1.75, None)
res = raiz_2.print_table()
print(f"\nPor lo tanto el valor que mas se aproxima a la segunda raiz con un error del 0.000001 es de {round(res, 5)}")

print("\nPrograma realizado por Luis Fernando Segobia Torres 2177528 a 17/08/2025")






















