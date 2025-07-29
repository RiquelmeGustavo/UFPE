"""
Arquivo: ufpe.ex23.py
Autor: Riquelme Gustavo
Descrição: Escreva uma função que retorne o n-ésimo termo da sequência de Fibbonaci, n dado.
"""

print('Sequência de Fibonacci')

n = int(input('Digite o número de termos: '))

def fibonacci(n):
    a = 0
    b = 1
    c = 0
    cont = 0

    if n > 0:
        while True:
            cont += 1
            a = b
            b = c
            c = a + b
            if cont == n:
                break
    return c

print(fibonacci(n))
