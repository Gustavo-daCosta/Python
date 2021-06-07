soma = 0
opcao = 'S'
while opcao != 'N':
    n = int(input('Digite um valor: '))
    soma += n
    opcao = str(input('Você deseja continuar?[S/N] ')).lower()
print(f'Soma total entre os valores digitados: {soma}')
n1 = 0
c = 1
while c != 0:
    n1 = int(input('Digite um valor: '))
print('FIM')