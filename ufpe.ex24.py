"""
Arquivo: ufpe.ex24.py
Autor: Riquelme Gustavo
Descrição: Seja z = y+ix, onde i² = -1, um número complexo. Construa um programa, de dado ze z2, com um menu de seleção que posso 
selecionar somar, diminuição, multiplicação, fazer o complexo conjugado de z, fazer módulo de z, fazer um produto interno de z, e z2, 
todas essas funcionalidade implementadas com funções.
"""


class Complexo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        if self.imaginario >= 0:
            return f"{self.real} + {self.imaginario}i"
        else:
            return f"{self.real} - {-self.imaginario}i"

def somar_complexos(z1, z2):
    return Complexo(z1.real + z2.real, z1.imaginario + z2.imaginario)

def subtrair_complexos(z1, z2):
    return Complexo(z1.real - z2.real, z1.imaginario - z2.imaginario)

def multiplicar_complexos(z1, z2):
    real_parte = (z1.real * z2.real) - (z1.imaginario * z2.imaginario)
    imaginario_parte = (z1.real * z2.imaginario) + (z1.imaginario * z2.real)
    return Complexo(real_parte, imaginario_parte)

def conjugado_complexo(z):
    return Complexo(z.real, -z.imaginario)

def modulo_complexo(z):
    return (z.real**2 + z.imaginario**2)**0.5

def produto_interno_complexos(z1, z2):
    return z1.real * z2.real + z1.imaginario * z2.imaginario

def menu_complexos():
    real1 = float(input("Digite a parte real de z1: "))
    imag1 = float(input("Digite a parte imaginária de z1: "))
    z1 = Complexo(real1, imag1)

    real2 = float(input("Digite a parte real de z2: "))
    imag2 = float(input("Digite a parte imaginária de z2: "))
    z2 = Complexo(real2, imag2)

    while True:
        print("\nEscolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Conjugado de z1")
        print("5. Módulo de z1")
        print("6. Produto interno de z1 e z2")
        print("0. Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            resultado = somar_complexos(z1, z2)
            print(f"Soma: {resultado}")
        elif opcao == '2':
            resultado = subtrair_complexos(z1, z2)
            print(f"Subtração: {resultado}")
        elif opcao == '3':
            resultado = multiplicar_complexos(z1, z2)
            print(f"Multiplicação: {resultado}")
        elif opcao == '4':
            resultado = conjugado_complexo(z1)
            print(f"Conjugado de z1: {resultado}")
        elif opcao == '5':
            resultado = modulo_complexo(z1)
            print(f"Módulo de z1: {resultado:.2f}")
        elif opcao == '6':
            resultado = produto_interno_complexos(z1, z2)
            print(f"Produto interno de z1 e z2: {resultado:.2f}")
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_complexos()
