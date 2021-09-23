import numpy as np
from numpy.linalg import solve

#declarando os coeficientes do sistema linear
a = float(input('Digite o coeficiente de x1: '))
b = float(input('Digite o coeficiente de y1: '))
print("\n")

c = float(input('Digite o coeficiente de x2: '))
d = float(input('Digite o coeficiente de y2: '))
print("\n")

#declarando os resultados do sistema linear
r1 = float(input('Digite o primeiro resultado: '))
r2 = float(input('Digite o segundo resultado: '))

#declarando as matrizes do sistema linear
A = np.array([[a,b],[c,d]])
B = np.array([[r1],[r2]])

#encontrando a matriz X
X = solve(A,B)
print("\n")

#imprimir os valores das incógnitas x e y
print('o valor de x é:',X[0])
print('o valor de y é:',X[1])
