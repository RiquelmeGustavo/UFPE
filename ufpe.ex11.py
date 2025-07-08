''' Escreva um programa para verificar se um triângulo de lados de comprimentos dados é retângulo, exibindo,
 nos casos afirmativos, sua hipotenusa e seus catetos. '''


a = float(input('Comprimento do primeiro lado: '))
b = float(input('Comprimento do segundo lado: '))
c = float(input('Comprimento do terceiro lado: '))


if a + b > c and a + c > b and b + c > a:
    hip = a
    co = b
    ca = c

    if b > a and b > c:
        hip = b
        co = a
        ca = c
    elif c > a and c > b:
        hip = c
        co = a
        ca = b

    if hip**2 == co**2 + ca**2:
        print(f'hip² = CO² + CA² \n{hip}² = {co}² + {ca}² \n{hip**2} = {co**2 + ca**2}')
        print('Os lados formam um triângulo Retângulo.')
    else:
        print('Os lados NÃO formam um triângulo Retângulo.')

else:
    print('Os lados não formam um triângulo.')
