"""
Arquivo: ufpe.ex20.py
Autor: Riquelme Gustavo
Descrição: Escreva um programa que transforme o computador numa urna eletrônica para eleição para presidente do país fictício, às quais concorrem 
os candidatos 83-Alibabá e 93-Alcapone. Cada voto deve ser dado pelo número do candidato, permitindo-se ainda o voto 00 para voto em branco. 
Qualquer voto diferente dos já citados é considerado nulo; em qualquer situação, o eleitor deve ser consultado quanto à confirmação do seu voto. 
No final da eleição, o programa deve emitir um relatório contendo a votação de cada candidato, a quantidade de votos em branco, a quantidade de 
votos nulos e o candidato eleito.
"""


print('Eleições para Presidente do Brasil')
print('83 - Alibabá \n93 - Alcapone')

alibaba = alcapone = nulo = branco = 0

while True:
    voto = int(input('Digite seu voto (-1 para terminar): '))
    confirmar = ''
    while 'S'!= confirmar != 'N':
        confirmar = str(input('Você confirma o seu voto? (S/N) ')).strip().upper()
    if confirmar == 'S':
        print('Voto confirmado.')
        if voto == -1:
            break
        elif voto == 00:
            branco += 1
        elif voto == 83:
            alibaba += 1
        elif voto == 93:
            alcapone += 1
        else:
            nulo += 1

print('---- Votação encerrada ----')
print(f'''Votos em Alibabá: {alibaba}
Votos em Alcapone: {alcapone}
Votos em Branco: {branco}
Votos Nulos: {nulo}''')

if alibaba > alcapone:
    eleito = 'Alibabá'
elif alcapone > alibaba:
    eleito = 'Alcapone'
else:
    eleito = 'Empate de votos. Nenhum candidato se elegeu.'

print(f'Candidato Eleito: {eleito}')
