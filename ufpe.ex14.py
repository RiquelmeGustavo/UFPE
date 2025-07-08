''' Escreva um programa para determinar as raízes reais ou complexas de uma equação do segundo grau,
dados os seus coeficientes. '''


from math import sqrt

print('ax² + bx + c = 0')

a = float(input('Coeficiente a: '))
b = float(input('Coeficiente b: '))
c = float(input('Coeficiente c: '))
D = b**2 - 4 * a * c

print(f'D = b² - 4ac \nD = {b}² - 4 * {a} * {c} \nD = {D:.2f}')

if D > 0:
    print('Existem duas raízes reais.')
    x1 = (-b + sqrt(D)) / (2 * a)
    print(f'x1 = -b + √D / 2 * a \nx1 = -({b}) + √{D:.2f} / 2 * {a} \nx1 = {x1:.2f}')
    x2 = (-b - sqrt(D)) / (2 * a)
    print(f'x2 = -b - √D / 2 * a \nx2 = -({b}) - √{D:.2f} / 2 * {a} \nx2 = {x2:.2f}')
elif D == 0:
    print('Existe uma raiz real.')
    print(f'x = -b / 2 * a \nx = -({b}) / 2 * {a}')
    x = -b / (2 * a)
    print(f'x = {x:.2f}')
elif D < 0:
    print('As raízes são complexas.')
