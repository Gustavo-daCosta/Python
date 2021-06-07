titulo = 'RODOVIÁRIA DO CENTRO'
print('-'*50)
print(f'{titulo:^50}')
print('-'*50)
print('Preço para viagem de 200km ou menos: R$0.50/km')
print('Preço para viagem de mais de 200km: R$0.45/km')
print('-'*50)
km = int(input('Distância a se percorrer em km: '))
if km <= 200:
    preco = km*0.50
else:
    preco = km*0.45
print(f'Preço total a se pagar: R${preco:.2f}')