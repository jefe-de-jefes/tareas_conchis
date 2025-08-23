"""LUIS FERNANDO SEGOBIA TORRES 2177528
A 12/08/2025
ESTE PROGRAMA RESUELVE UN SISTEMA DE
ECUACIONES TRIANGULAR INFERIOR"""

input('\n**********SISTEMA RESOLVEDOR DE SISTEMA********\n********DE ECUACIONES TRIANGULAR INFERIOR******')

n:int = int(input('\nIntroduzca el numero entero total de ecuaciones o variables: '))

matriz = [[0]*n for _ in range(n)]
b = []

for i in range(n):
    print(f'\n***Datos de la ecuacion {i+1}***')
    for j in range(i+1):
        value = int(input(f'Introduzca el valor del coeficiente de la X{j+1} para la pos [{i+1}, {j+1}] de la matriz: '))
        matriz[i][j] = value
    b.append(int(input(f'Introduzca el resultado b{i+1}: ')))

res_x = []

for i in range(n):
    pre_res:float = b[i]
    for j in range(i):
        pre_res -= matriz[i][j] * res_x[j]
    res_x.append(pre_res/matriz[i][i])

print('\nMATRIZ')
for i in range(n):
    for j in range(n):
        print(f'{matriz[i][j]}x_{j+1}', end = ' ')
    print(f'= {b[i]}')

print('\nRESULTADOS')
for i in range(n):
    print(f'Resultado de x_{i+1}= {res_x[i]}')
