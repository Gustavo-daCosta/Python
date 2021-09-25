valor, notas50, notas20, notas10, notas1 = 0, 0, 0, 0, 0
print('=-='*20)
print('         CAIXA ELETRÔNICO')
print('=-='*20)
while True:
    valor = int(input('Digite o valor que você deseja sacar: R$'))
    while valor >= 50:
        valor -= 50
        notas50 += 1
    while valor >= 20:
        valor -= 20
        notas20 += 1
    while valor >= 10:
        valor -= 10
        notas10 += 1
    while valor >= 1:
        valor -= 1-
        notas1 += 1
    if valor == 0:
        break
print('=-='*20)
if notas50 >= 1:
    print(f'Total de {notas50} cédulas de R$50')
if notas20 >= 1:
    print(f'Total de {notas20} cédulas de R$20')
if notas10 >= 1:
    print(f'Total de {notas10} cédulas de R$10')
if notas1 >= 1:
    print(f'Total de {notas1} cédulas de R$1')
print('=-='*20)
print('PROCESSO FINALIZADO! Tenha um bom dia!')