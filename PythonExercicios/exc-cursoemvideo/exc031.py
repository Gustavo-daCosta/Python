km = int(input('Digite a distância em km: '))
if km <= 200:
    print('Valor cobrado por KM rodado: R$0,50')
    print(f'O valor da viagem é de R${km*0.50}')
else:
    print('Valor cobrado por KM rodado: R$0,45')
    print(f'O valor da viagem é de R${km*0.45}')
