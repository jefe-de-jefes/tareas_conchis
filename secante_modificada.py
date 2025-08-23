
"""LUIS FERNANDO SEGOBIA TORRES 2177528
A 20/08/2025
ESTE PROGRAMA CALCULA UNA RAIZ REAL CON EL METODO
de la secante modificada"""

import os
import math

def cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

def format(num):
        return "------    " if num is None else f"{num:<10.8f}"

def print_registro(x_i, x_iPlus, error):
    print(f"{format(x_i)} | {format(x_iPlus)} | {format(error)}")

def f_plus(x_i, delta:float) -> float:
    return x_i - ((delta*f_x(x_i)) / (f_x(x_i + delta) - f_x(x_i)))

def f_x(x:float) -> float:
    return x/2 + 2 * math.log(x) - 50

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
        while(self.error > 0.000001):
            self.x_iPlus = f_plus(self.x_i, self.delta)
            self.error = f_error(self.x_i, self.x_iPlus)
            print_registro(self.x_i, self.x_iPlus, self.error)
            self.x_i = self.x_iPlus
        return self.x_iPlus


cleaner()
print('\n*******METODO DE LA SECANTE MODIFICADA********\n*************CALCULA RAICES REALES************\n')
print("Siendo f(x) = x/2 + 2*ln(x) - 50 una funcion continua, se obtendran las raices aproximadas con un error delta = 0.01 y un x_0 = 85")

raiz_1 = Raices(0.01, 85)
res = raiz_1.print_table()
print(f"\nPor lo tanto el valor que mas se aproxima a la primer raiz es de {round(res, 5)}")

print("\nPrograma realizado por Luis Fernando Segobia Torres 2177528 a 20/08/2025")

