
# LUIS FERNANDO SEGOBIA TORRES 2177528
# A 24/08/2025
# ESTE PROGRAMA RESUELVE EL SISTEMA DE ECUACIONES NO LINEALES VISTO EN CLASE

import os
import math

def cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

def format(num):
        return "------    " if num is None else f"{num:<10.8f}"

def print_registro(x_i, y_i, x_iPlus, y_iPlus, x_error, y_error):
    print(f"{format(x_i)} | {format(y_i)} | {format(x_iPlus)} | {format(y_iPlus)} | {format(x_error)} | {format(y_error)}")

def fx_plus(x_i, y_i) -> float:
    return x_i - (f_u(x_i,y_i)*(1+6*x_i*y_i) - f_v(x_i,y_i)*x_i) / ((2*x_i+y_i)*(1+6*x_i*y_i) - x_i*3*y_i**2)

def fy_plus(x_i, y_i) -> float:
    return y_i - (f_v(x_i,y_i)*(2*x_i+y_i)-f_u(x_i,y_i)*(3*y_i**2)) / ((2*x_i+y_i)*(1+6*x_i*y_i) - x_i*3*y_i**2)

def f_u(x:float, y:float) -> float:
    return x**2 + x*y -10

def f_v(x:float, y:float) -> float:
    return y + 3*x*y**2 - 57

def fx_error(x_i, x_iPlus) ->float:
    return abs((x_iPlus - x_i ) / x_iPlus)

def fy_error(y_i, y_iPlus):
    return abs((y_iPlus - y_i) / y_iPlus)

class Raices:
    def __init__(self, x_i, y_i, x_iPlus = None, y_iPlus = None, x_error = 100, y_error = 100):
        self.x_i = x_i
        self.y_i = y_i
        self.x_iPlus = x_iPlus
        self.y_iPlus = y_iPlus
        self.x_error = x_error
        self.y_error = y_error

    def print_table(self)->float:
        print('\n*****Tabla de resultados*****\n')
        print(f' {"x_i":<10} | {"y_i":<10} | {"x_i+1":<10} | {"y_i+1":<10} | {"x_error":<10} | {"y_error":<10}')
        for _ in range(50):
            print('-', end = '')
        print()
        while(self.x_error > 0.000001 and self.y_error > 0.000001):
            self.x_iPlus = fx_plus(self.x_i, self.y_i)
            self.x_error = fx_error(self.x_i, self.x_iPlus)
            self.y_iPlus = fy_plus(self.x_i, self.y_i)
            self.y_error = fy_error(self.y_i, self.y_iPlus)
            print_registro(self.x_i, self.y_i, self.x_iPlus, self.y_iPlus, self.x_error, self.y_error)
            self.x_i = self.x_iPlus
            self.y_i = self.y_iPlus
        return self.x_iPlus, self.y_iPlus


cleaner()
print('*** SISTEMA PARA SOLUCIONAR SISTEMA *** \n****** DE ECUACIONES NO LINEALES ******')
print('Siendo u = x**2 + xy -10 = 0')
print('Y v = y + 3xy**2 -57 = 0')
print('Se utilizara el metodo de Newton-Raphson')

print('En el sistema existen 2 soluciones, dentro del cuadrante 1 y 4')
x = float(input('Introduzca el x inicial x_0: '))
y = float(input('Introduzca el y inicial y_0: '))
print(f'\nSe utilizara como x_0 = {x} y y_0 = {y}')

raiz_1 = Raices(x,y)
res_x, res_y = raiz_1.print_table()
print(f"\nLa primer solucion del sistema de ecuaciones no lineales son con x =  {round(res_x, 5)} y y = {round(res_y, 5)}")

print("\nPrograma realizado por Luis Fernando Segobia Torres 2177528 a 25/08/2025")

