"""
Arquivo: ufpe.ex08.py
Autor: Riquelme Gustavo
Descrição: Construir um programa para ordenar 3 números dados.
"""


x = float(input('Primeiro número: '))
y = float(input('Segundo número: '))
z = float(input('Terceiro número: '))

maior = x
if y > x and y > z:
    maior = y
elif z > x and z > y:
    maior = z

meio = x
if y > x and y < z or y < x and y > z:
    meio = y
elif z > x and z < y or z < x and z > y:
    meio = z

menor = x
if y < x and y < z:
    menor = y
elif z < x and z < y:
    menor = z

print(f'{menor}, {meio}, {maior}')
