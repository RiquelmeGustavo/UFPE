"""
Arquivo: ufpe.ex06.py
Autor: Riquelme Gustavo
Descrição: Faça um programa para calcular as médias finais de um aluno, dizer se o mesmo está aprovado e, caso contrário,
afirmar se o mesmo vai para a final e calcular sua média final e afirmar sua aprovação ou reprovação.
"""


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4

print(f'Média: {media:.1f}')

if media >= 7:
    print('APROVADO!')
elif 3 <= media < 7:
    print('Vai para Final!')
    final = float(input('Nota da prova Final: '))
    media_final = (media + final) / 2
    if media_final >= 7:
        print(f'Média Final: {media_final} \nAPROVADO na final!')
    else:
        print(f'Média Final: {media_final} \nREPROVADO na final!')
elif media < 3:
    print('REPROVADO DIRETO!')
