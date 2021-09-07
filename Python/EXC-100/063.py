soma = cont = par = 0
opcao = 'S'
while opcao != 'N':
    cont += 1
    print(f'{cont}° NÚMERO'.center(40, '-'))
    num = int(input('Digite um número: '))
    soma += num
    if cont == 1:
        menor = num
        maior = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    if num % 2 == 0:
        par += 1
    opcao = str(input('Deseja continuar? [S/N]: ')).upper()
print('RESULTADOS'.center(40, '='))
print(f'''Somatório entre todos os valores: {soma}
Menor valor digitado: {menor}
Maior valor digitado: {maior}
Média dos valores: {soma/cont:.1f}
Total de valores pares: {par}''')