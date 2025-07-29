"""
Arquivo: ufpe.ex19.py
Autor: Riquelme Gustavo
Descrição: A série harmônica S(n), com n sendo um inteiro, é uma serie divergente. Isto significa que dado qualquer real k 
existe um n0 tal que S(n0) > k. Escreva um programa que dado um real k determine o menor inteiro no tal que S(no) > k. 
Por exemplo se k=2, o programa deve fornecer n0 = 4, pois S(4) = 2,083... e S(3) = 1,8333...

S(n) = 1/i = 1 + 1/2 + 1/3 +...+ 1/n
"""


k = int(input('Digite o valor de k: '))
S = n0 = 1

print(f'S({n0}) = {S}')

while True:
    n0 += 1
    print(f'S({n0}) = {S:.2f} + 1/{n0} = ', end='')
    S = S + 1/n0
    print(f'{S:.3f}')
    if S > k:
        break

print(n0)
