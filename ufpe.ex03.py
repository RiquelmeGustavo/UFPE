"""
Arquivo: ufpe.ex01.py
Autor: Riquelme Gustavo
Descrição: Construir um programa para calcular o valor do salário de um professor que ganha por hora aula HA
e trabalha HT de horas por mês, decontando o valor do INSS que é de D por cento do seu salário total.
"""


HA = float(input('Valor da hora/aula: '))
HT = float(input('Horas trabalhadas por mês: '))
salario = HA * HT

if salario <= 1500:
    INSS = salario * 7.5/100
elif 1500 < salario <= 2800:
    INSS = salario * 9/100
elif 2800 < salario <= 4100:
    INSS = salario * 12/100
elif 4100 < salario <= 8100:
    INSS = salario * 14/100

if salario <= 8100:
    salario -= INSS
    print(f'Salário: R$ {salario:.2f}')
elif salario > 8100:
    print(f'Salário: R$ {salario:.2f}')
    print('O salário ultrapassa o teto do INSS. Não é descontado.')
