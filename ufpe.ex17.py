"""
Arquivo: ufpe.ex17.py
Autor: Riquelme Gustavo
Descrição: Um número inteiro é dito perfeito se o dobro dele é igual à soma de todos os seus divisores.
Por exemplo, como os divisores de 6 são 1, 2, 3 e 6 e 1 + 2 + 3 + 6 = 12, 6 é perfeito. A matemática ainda não sabe
se a quantidade de números perfeitos é ou não finita. Escreva um programa que liste todos os números perfeitos menores
que um inteiro n dado.
""" 


num = int(input('Digite um número para ver os perfeitos anteriores: '))
cont = soma = 0
n = 1

while True:
    cont += 1
    if n % cont == 0:
        soma += n/cont
    if cont == n:
        perfeito = soma == n * 2
        if perfeito == True:
            print(n)
        n += 1
        cont = soma = 0
    if n == num:
        break
