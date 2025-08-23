
"""LUIS FERNANDO SEGOBIA TORRES 2177528
A 14/08/2025
ESTE PROGRAMA CALCULA UNA RAIZ REAL CON EL METODO
DE PUNTO FIJO"""

import os
import math

def cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

def format(num):
        return "------    " if num is None else f"{num:<10.7f}"

def print_table(x_i, x_iPlus, error):
    print(f"{format(x_i)} {format(x_iPlus)} {format(error)}")

def f_x(x:float) -> float:
    return math.e ** x / math.pi

def f_error(x_i, x_iPlus) ->float:
    return abs((x_iPlus - x_i )/ x_iPlus)

cleaner()

print('\n*******METODO DE PUNTO FIJO QUE********\n********CALCULA RAICES REALES**********\n')
print("Siendo f(x) = e**x - pi*x una funcion continua, g(x) quedaria como e**x / pi, se obtendra una raiz aproximada con un error del 0.000001")

x_i:float = 0.6
x_iPlus:float = None
error:float = 100;

print('\n*****Tabla de resultados*****\n')
print(f'{"x_i":<10} {"x_i+1":<10} {"error":<10}')
while(error > 0.000001):
    x_iPlus = f_x(x_i)
    error = f_error(x_i, x_iPlus)
    print_table(x_i, x_iPlus, error)
    x_i = x_iPlus


print(f"\nPor lo tanto el valor que mas se aproxima a la raiz con un error del 0.000001 es de {x_iPlus}")

print("\nPrograma realizado por Luis Fernando Segobia Torres 2177528 a 14/08/2025")
