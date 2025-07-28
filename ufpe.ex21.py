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
