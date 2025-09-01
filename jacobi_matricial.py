"""LUIS FERNANDO SEGOBIA TORRES 2177528
A 31/08/2025
ESTE PROGRAMA CALCULA LA SOLUCION DE UN SISTEMA DE N ECUACIONES CON N VARIABLES"""

import os
import math
import numpy as np
import re

def parse_equation(eq, variables):

    izq, der = eq.split("=")
    der = float(der.strip())

    coef = [0.0] * len(variables)

    terminos = re.findall(r'([+-]?\d*\.?\d*)\s*(x_\d+)', izq.replace(" ", ""))

    for num, var in terminos:
        if num in ("", "+"):
            num = 1.0
        elif num == "-":
            num = -1.0
        else:
            num = float(num)
        coef[variables.index(var)] += num

    return coef, der


def cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

def format(X):
    return ' | '.join(f'{num:<11.8f}' for num in X)

def f_error(x_i, x_iPlus) ->float:
    return abs((x_iPlus - x_i ) / x_iPlus)

class Solucion:
    def __init__(self, n, D_inv, b, R, X_act, error = 100, tolerancia = 0.000001):
        self.n = n
        self.D_inv = D_inv
        self.b = b
        self.R = R
        self.X_act = X_act
        self.error = error
        self.tolerancia = tolerancia

    def X_next(self):
        return self.D_inv @ (self.b - self.R @ self.X_act)

    def iteracion(self):
        i = 0
        print()
        encabezado = 'ITERACION'.ljust(14) + ' | ' + ' | '.join(v.ljust(11) for v in variables)
        print(encabezado)
        while self.error > self.tolerancia:
            X_new = self.X_next()
            self.error = max(abs(X_new - self.X_act)/ X_new)
            self.X_act = X_new
            i += 1
            print(f'Iteracion #{i:<3} = {format(self.X_act)}', )
        return self.X_act



if __name__ == "__main__":
    cleaner()
    print('\n*******METODO MATRICIAL DEL********\n*******METODO DE JACOBI********\n')
    n = 0
    while True:
        try:
            n = int(input("Ingrese el numero de variables o ecuaciones de la matriz (n x n): "))
            if n > 0:
                variables = [f"x_{i+1}" for i in range(n)]
                break
            else:
                print("El tamaño debe ser un entero positivo.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    A = np.zeros((n, n), dtype=float)
    b = np.zeros(n)

    print(f"\nIngrese las {n} ecuaciones del sistema (ejemplo: 2x_1 + 3x_2 - x_3 = 5):")
    for i in range(n):
        while True:
            eq = input(f"Ecuación {i+1}> ")
            try:
                coef, independiente = parse_equation(eq, variables)
                A[i] = coef
                b[i] = independiente
                break
            except ValueError:
                print("Error: Uno de los valores no es un número válido. Intente de nuevo.")


    try:
        if np.linalg.det(A) == 0:
            print('La matriz tienen un det(A) = 0, por lo tanto el sistema de ecuaciones no tiene una solucion unica.')
            exit()

        #inicializar vector inicial de supuesta respuesta
        print('Introduzca el vector inicial con el que se va a trabajar.')
        X_act = np.zeros(n)
        for i in range(n):
            X_act[i] = float(input(f"Valor inicial de x{i+1}: "))

        print(f"Vector inicial X:\n { ' | '.join(v.ljust(11) for v in variables) }\n {format(X_act)}")
        print("\nResolviendo el sistema...")

        D = np.diag(np.diag(A))
        R = A - D
        D_inv = np.linalg.inv(D)

        sol = Solucion(n, D_inv, b, R, X_act)
        res = sol.iteracion()


        print("\nPor lo tanto el valor que más se aproxima a la solución del sistema con un error del 0.000001 es de:")
        print(' | '.join(v.ljust(11) for v in variables))
        print(f'{format(res)}')

    except ValueError as e:
        print(f"\nError al resolver el sistema: {e}")
        print("La matriz puede ser singular (no tener solución única).")



print("\nPrograma realizado por Luis Fernando Segobia Torres 2177528 a 30/08/2025")
