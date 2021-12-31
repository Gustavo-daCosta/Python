from random import randint
vetor, soma = list(), 0

while True:
    for c in range(0, 15):
        vetor.append(randint(1, 15))
    num = int(input('Digite um valor entre 1 e 15: '))
    if num in vetor:
        break
    else:
        print('Este número não foi sorteado, tente novamente.')
print('NÚMERO\tPOSIÇÃO')
for c in range(0, 15):
    if vetor[c] == num:
        print(f'  {num}\t  {c}')
        soma += 1
print('-'*40)
print(f'Total de vezes que o número {num} foi sorteado: {soma} vezes')