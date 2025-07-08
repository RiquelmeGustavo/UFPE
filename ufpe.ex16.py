''' Escreva um programa para calcular a soma dos n primeiros termos das sequências abaixo, n dado.
a) (1/2, 3/5, 5/8,...)   b) (1, -(1/2), (1/3), -(1/4),...) '''


# A

termos = int(input('Digite o número de termos: '))
numerador = 1
denominador = 2
cont = soma = 0

print(f'{numerador}/{denominador}', end='')

while True:
    cont += 1
    num = numerador / denominador
    soma += num
    numerador += 2
    denominador += 3
    if cont == termos:
        break
    print(f' + {numerador}/{denominador}', end='')


print()
print(f'= {soma:.2f}')
