# Escreva um programa para determinar o maior de três números dados.

x = float(input('Primeiro número: '))
y = float(input('Segundo número: '))
z = float(input('Terceiro número: '))

maior = x
if y > x and y > z:
    maior = y
elif z > x and z > y:
    maior = z

print(f'Maior: {maior}')
