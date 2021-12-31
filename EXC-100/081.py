lista, pessoa25, posicao = list(), list(), list()
soma = maior = 0

for c in range(0, 8):
    print(f'{c+1}° PESSOA'.center(50, '-'))
    idade = int(input('Idade: '))
    lista.append(idade)
    soma += idade
    if idade > 25:
        pessoa25.append(c+1)
    if c == 0:
        maior = idade
    else:
        if idade > maior:
            maior = idade
for c in range(0, 8):
    num = lista[c]
    if num == maior:
        posicao.append(c)
    else:
        break
print('-'*50)
print(f'''Média de idade das pessoas registradas: {soma/8:.2f} anos
Posições das pessoas com mais de 25 anos: {pessoa25}
Maior idade registrada: {maior} anos
Posições em que a maior idade foi digitada: {posicao}''')