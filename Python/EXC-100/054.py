soma = peso90 = peso50 = peso100 = 0
for c in range(1, 8):
    print(f'{c}° PESSOA'.center(40, '-'))
    peso = int(input('Digite o seu peso: '))
    altura = float(input('Digite sua altura: '))
    soma += altura
    if peso > 90:
        peso90 += 1
    if peso < 50 and altura < 1.60:
        peso50 += 1
    if peso > 100 and altura > 1.90:
        peso100 += 1
media = soma/7
print('-'*40)
print(f'''Média de altura do grupo: {media:.2f}
Pessoas que pesam mais de 90Kg: {peso90} pessoas
Pessoas que pesam menos de 50Kg e tem menos de 1.60m: {peso50} pessoas
Pessoas que pesam mais de 100Kg e tem mais de 1.90m: {peso100} pessoas''')