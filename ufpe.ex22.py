"""
Arquivo: ufpe.ex22.py
Autor: Riquelme Gustavo
Descrição: Fatorial ímpar de um número n ímpar positivo é o produto de todos os números ímpares positivos 
menores do que ou iguais a n. Indicando o fatorial ímpar de n por n temos, n = 1 . 3. 5..... n. 
Por exemplo, 7 = 1.3.5.7 = 105. Escreva funções para a determinação do fatorial ímpar de um inteiro ímpar dado.
"""


print('Fatorial Ímpar')

n = int(input('Digite um número ímpar de termos: '))

def fatorial_impar(n):
    if n % 2 == 0:
        return 'Erro. O número deve ser ímpar.'
    if n < 1:
        return 'Erro. O número deve ser positivo.'

    resultado = 1
    for i in range(1, n + 1, 2):
        resultado *= i
    return resultado

print(fatorial_impar(n))
