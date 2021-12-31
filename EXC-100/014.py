titulo = 'LOCADORA DE CARROS'
print('=-='*30)
print(f'{titulo:^90}')
print(f'=-='*30)
dias = int(input('Digite a quantidade de dias em que o carro foi alugado: '))
km = int(input('Digite quantos Km foram rodados: '))
total = (dias * 90) + (km * 0.20)
print(f'Valor cobrado pelo dias alugados: R${dias*90:.2f}       Valor cobrado pelos Km rodados: R${km*0.20:.2f}')
print(f'Valor total a ser cobrado: R${total:.2f}')