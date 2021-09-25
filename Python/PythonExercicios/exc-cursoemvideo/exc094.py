dados = dict()
lista, mulheres = list(), list()
opcao = pessoas = media = acimaMedia = total = 0
while True:
    pessoas += 1
    lista.append(str(input('Nome: ')))
    lista.append(str(input('Sexo: [M/F]: ')))
    lista.append(int(input('Idade: ')))
    total += lista[2]
    if lista[1] == 'F':
        mulheres.append(lista[0])
    dados[f'pessoa{pessoas}'] = lista[:]
    lista.clear()
    opcao = str(input('Deseja continuar? [S/N]: '))
    if opcao in 'Nn':
        break
media = total/pessoas
print('=-='*20)
print(f'- O grupo tem {pessoas} pessoas.')
print(f'- A média de idade é de {media:.2f}')
print(f'- As mulheres cadastradas foram: {mulheres}')
for c in range(0, len(mulheres)):
    print(mulheres[c], end='')
print()
print('- Lista de pessoas que estão acima da média: ')
for c in range(0, pessoas):
    if dados[f'pessoa{c+1}'][2] > media:
        print(f'Nome: {dados[f"pessoa{c+1}"][0]}; Sexo: {dados[f"pessoa{c+1}"][1]}; Idade: {dados[f"pessoa{c+1}"][2]}')
print('<<< ENCERRADO >>>')