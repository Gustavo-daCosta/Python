velocidade = int(input('Digite a velocidade do carro em Km/h: '))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade e foi multado!')
    print(f'Valor da multa: R${(velocidade-80)*5:.2f}')
else:
    print('Você está dentro do limite de velocidade e não será multado.')