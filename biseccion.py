
"""LUIS FERNANDO SEGOBIA TORRES 2177528
A 13/08/2025
ESTE PROGRAMA CALCULA UNA RAIZ REAL DADA
DE LA F(X) | F:F->R SIENDO F UNA F CONTINUA
EN [A,B] Y ADEMAS F(A)*F(B) < 0"""

import os
import math

def cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

def format(num):
        return "------    " if num is None else f"{num:<10.7f}"

def print_table(a, b, x_i, x_iPlus, error):
    print(f"{format(a)} {format(b)} {format(x_i)} {format(x_iPlus)} {format(error)}")

def f_x(x:float) -> float:
    return x * math.e ** x - math.pi


cleaner()

print('\n*******METODO DE BISECCION QUE********\n********CALCULA RAICES REALES******\n')
print("Siendo f(x) = x*e**x - pi una funcion continua, se obtendra una raiz aproximada con un error del 0.000001")

a:float = 0
b:float = 2
x_i:float = None
x_iPlus:float = None
error:float = 100;

print('\n*****Tabla de resultados*****\n')
print(f'{"a":<10} {"b":<10} {"x_i":<10} {"x_i+1":<10} {"error":<10}')
while(error > 0.000001):
    x_iPlus = (a+b)/2
    if(x_i!=None):
        error = abs((x_iPlus - x_i)/x_iPlus)
        print_table(a, b, x_i, x_iPlus, error)
    else:
        print_table(a, b, x_i, x_iPlus, None)
    x_i = x_iPlus
    if(f_x(a) * f_x(x_iPlus) < 0):
        b = x_iPlus
    else:
        a = x_iPlus

print(f"\nPor lo tanto el valor que mas se aproxima a la raiz con un error del 0.000001 es de {x_iPlus}")

print("\nPrograma realizado por Luis Fernando Segobia Torres 2177528 a 13/08/2025")








































