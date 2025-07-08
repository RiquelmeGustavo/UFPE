# Identifique um programa que diz quantos dias tem um determinado mês e faça um programa.


mes = str(input('Digite o nome de um mês: ')).strip().title()

if mes in ['Janeiro', 'Março', 'Maio', 'Julho', 'Agosto', 'Outubro', 'Dezembro']:
    dias = 31
elif mes in ['Abril', 'Junho', 'Setembro', 'Novembro']:
    dias = 30
elif mes == 'Fevereiro':
    dias = '28 ou 29'

print(f'{mes} tem {dias} dias.')
