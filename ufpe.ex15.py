"""
Arquivo: ufpe.ex15.py
Autor: Riquelme Gustavo
Descrição: Escreva um programa que determine a soma dos quadrados dos n primeiros números naturais, n dado.
""" 


termos = int(input('Quantidade de termos: '))
num = 1
soma = 0

print(f'{num}²', end='')

while True:
    soma += num**2
    if num == termos:
        break
    num += 1
    print(f' + {num}²', end='')

print()
print(f'Soma dos quadrados dos números: {soma}')
