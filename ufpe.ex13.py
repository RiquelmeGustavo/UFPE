''' Desenvolva um aplicativo para que calcule a média de três notas acadêmicas em uma disciplina
semestral de um discente da Universidade X. Observando esse resultado analise se:

a) Teve aprovação (media >= 7,00)
b) Teve que fazer uma final (3,00 <= media < 7,00) e depois da nota da final se obteve a
aprovação na final ( (media+prova final)/2 >= 5,00)
c) Se teve reprovação direta (media <3,00). '''


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
media = (n1 + n2 + n3) / 3

print(f'Média: {media:.1f}')

if media >= 7:
    print('Aprovado!')

elif 3 <= media < 7:
    print('Você vai para Final.')
    final = float(input('Nota da Final: '))
    media_final = (media + final) / 2

    print(f'Média Final: {media_final:.1f}')

    if media_final >= 5:
        print('Aprovado na Final!')
    else:
        print('Reprovado na Final!')

elif media < 3:
    print('Reprovado direto!')
