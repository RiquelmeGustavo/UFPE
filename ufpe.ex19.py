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
