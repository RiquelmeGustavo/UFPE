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
