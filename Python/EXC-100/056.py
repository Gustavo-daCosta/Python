soma = cont = 0
while True:
    num = int(input('Digite um número [1111 para interromper]: '))
    soma += num
    cont += 1
    if num == 1111:
        break
print('-'*30)
print(f'No total foram digitados {cont} valores.')
print(f'Soma de todos os valores: {soma}')