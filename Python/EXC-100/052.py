soma = maior = menos5 = mais18 = 0
for c in range(1, 11):
    print(f'{c}° PESSOA'.center(40, '-'))
    idade = int(input('Digite a idade: '))
    soma += idade
    if c == 1:
        maior = idade
    if idade > maior:
        maior = idade
    if idade > 18:
        mais18 += 1
    if idade < 5:
        menos5 += 1
media = soma/10
print(f'Média de idade do grupo: {media:.1f} anos')
print(f'Pessoas maiores de 18 anos: {mais18} pessoas')
print(f'Pessoas menores de 5 anos: {menos5} pessoas')
print(f'Maior idade lida: {maior} anos')