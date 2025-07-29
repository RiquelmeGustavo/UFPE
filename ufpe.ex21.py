"""
Arquivo: ufpe.ex21.py
Autor: Riquelme Gustavo
Descrição: Os sistemas de computação que gerenciam caixas de lojas e supermercados fornecem ao
operador, após a informação do valor do pagamento, o troco, em números decimais, que ele deve
dar ao cliente. Talvez fosse interessante que, para otimizar a utilização das notas e das moedas de
menor valor, visando a minimizar o problema da "falta de troco", o sistema fornecesse ao operador
as quantidades de cada nota e de cada moeda para um "troco ótimo". Admitindo que o
supermercado forneça também troco para de qualquer valor, escreva um programa que, recebendo
o valor da compra e o valor do pagamento, forneça o "troco ótimo" no sentido comentado acima.
"""


compra = float(input('Valor da compra: '))
pagamento = float(input('Valor do pagamento: '))
troco = pagamento - compra
cedula = 100
total = 0

if troco < 0:
    print(f'Você está devendo R$ {troco}')
elif troco <= 0.05:
    print('Compra finalizada. Volte sempre!')
else:
    print('Troco ótimo:')
    while True:
        if troco >= cedula:
            troco -= cedula
            total += 1
        else:
            if total > 0 and cedula >= 1:
                print(f'{total} cédulas de R$ {cedula:.2f}')
            elif total > 0 and cedula < 1:
                print(f'{total} moedas de R$ {cedula:.2f}')
            if cedula == 100:
                cedula = 50
            elif cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 5
            elif cedula == 5:
                cedula = 2
            elif cedula == 2:
                cedula = 1
            elif cedula == 1:
                cedula = 0.50
            elif cedula == 0.50:
                cedula = 0.25
            elif cedula == 0.25:
                cedula = 0.20
            elif cedula == 0.20:
                cedula = 0.10
            elif cedula == 0.10:
                cedula = 0.05
            total = 0
            if troco < 0.05:
                break
