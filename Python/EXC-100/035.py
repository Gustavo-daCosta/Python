print('=-='*15)
print('ALUGUEL DE CARROS'.center(45))
print('=-='*15)
while True:
    print('Tipos de carros: Popular ou Luxo')
    carro = str(input('Tipo de carro: ')).lower()
    if carro not in 'popularluxo':
        print(f'ERRO! {carro} não é um tipo de carro.')
    else:
        break
dias = int(input('Por quantos dias o carro foi alugado? '))
km = int(input('Quantos Km foram percorridos? '))
if carro == 'popular':
    aluguel = dias*90
    if km <= 100:
        percorrido = km*0.20
    else:
        percorrido = km*0.10
else:
    aluguel = dias*150
    if km <= 200:
        percorrido = km*0.30
    else:
        percorrido = km*0.25
print('=-='*15)
print(f'Valor do aluguel: R${aluguel:.2f}')
print(f'Valor da quilometragem: R${percorrido:.2f}')
print(f'Valor total a se pagar: R${aluguel+percorrido:.2f}')