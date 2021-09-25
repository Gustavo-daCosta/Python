velo = int(input('Digite a velocidade do carro em km/h: '))
if velo > 80:
    print('Você excedeu o limite de velocidade e será multado.')
    multa = (velo - 80)*7
    print(f'Você recebeu uma multa no valor de R${multa},00')
else:
    print('Você está dentro do limite de velocidade.')