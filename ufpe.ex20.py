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
