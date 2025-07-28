"""
Arquivo: ufpe.ex05.py
Autor: Riquelme Gustavo
Descrição: Construir um programa que tire o módulo de um vetor tridimensional.
"""


from math import sqrt

print('Calcular o Módulo de um Vetor')
print('v = (x, y, z)')

x = int(input('Coordenada x: '))
y = int(input('Coordenada y: '))
z = int(input('coordenada z: '))
v = sqrt(x**2 + y**2 + z**2)

print(f'v = ({x}, {y}, {z})')
print(f'[v] = {v:.2f}')
