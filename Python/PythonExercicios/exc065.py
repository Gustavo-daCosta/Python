media = 0
maior = 0
menor = 0
n = 0
cont = 0
opcao = 'S'
while opcao == 'S':
    n = int(input('Digite um número inteiro: '))
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    media += n
    opcao = str(input('Você deseja continuar? [S/N] '))
print(f'A média entre todos os valores digitados é {(media/cont):.2f}')
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')