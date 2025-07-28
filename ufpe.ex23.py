"""
Arquivo: ex018ufpe.py
Descrição: Cálculo do volume de um paralelepípedo.
Autor: Riquelme Gustavo
"""


def volume(h, b, l):
    return h * b * l

h = float(input('Digite a altura: '))
b = float(input('Digite a base: '))
l = float(input('Digite o comprimento: '))

v = volume(h, b, l)

print(f'Volume = {v}')
