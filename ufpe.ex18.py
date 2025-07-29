"""
Arquivo: ufpe.ex18.py
Autor: Riquelme Gustavo
Descrição: A sequência de Fibonacci é a sequência (1, 1, 2, 3, 5, 8, 13,...)
definida por: an = {1 se n=1 ou n=2}{an-1 + an-2 se n>2}. Escreva um programa que determine o n-ésimo termo desta
sequência, n dado.
""" 


print('Sequência de Fibonacci')

num = int(input('Digite o número de termos: '))
a = 0
b = 1
c = 0
cont = 0

if num > 0:
    while True:
        cont += 1
        a = b
        b = c
        c = a + b
        print(f'-> {c} ', end='')
        if cont == num:
            break
