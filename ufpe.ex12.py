''' Dados três comprimentos, seja X1, X2 e X3, crie um algorítimo que afirme se estes formam um triângulo. Sendo um
triângulo implemente o cálculo do seu perímetro e área e faça sua classificação em equilátero, isósceles e escaleno.
Utilize a fórmula de Heron para o cálculo do perímetro (Perímetro 2p = (X1+X2+X3)
e a área é A = [p(p-X1)(p-X2)(p-X3)]1/2). '''


from math import sqrt

a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('comprimento da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        triangulo = 'Equilátero'
    elif a == b != c or a == c != b or b == c != a:
        triangulo = 'Isósceles'
    elif a != b != c != a:
        triangulo = 'Escaleno'

    P = a + b + c
    p = (a + b + c) / 2
    A = sqrt(p * (p - a)*(p - b)*(p - c))

    print(f'As retas formam um triângulo {triangulo}.')
    print(f'Perímetro = {P}')
    print(f'Área = {A:.2f}')

else:
    print('As retas NÃO formam um triângulo.')
