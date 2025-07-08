''' Escreva um programa que realize arredondamentos de números utilizando a regra usual da matemática: se a parte
fracionária for maior do que ou igual a 0,5, o número é arredondado para o inteiro imediatamente superior,
caso contrário, é arredondado para o inteiro imediatamente inferior. '''


num = float(input('Digite um número: '))
inteiro = int(num)
decimal = num - inteiro

if decimal < 0.5:
    print(inteiro)
elif decimal >= 0.5:
    print(inteiro + 1)
