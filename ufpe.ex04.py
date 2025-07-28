"""
Arquivo: ufpe.ex04.py
Autor: Riquelme Gustavo
Descrição: Construir um programa que faça a conversão de temperatura de Celcius para Fahrenheit. (F = 9 * C / 5 + 32)
"""


print('Converter Celcius em Fahrenheit')

C = float(input('Digite a temperatura em °Celcius: '))
F = (9 * C / 5) + 32

print(f'Fahrenheit: {F} °F')
