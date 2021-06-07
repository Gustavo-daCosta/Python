print('=-='*15)
print('     CÁLCULO DE IMC')
print('=-='*15)
alt = float(input('Digite sua altura: '))
peso = int(input('Digite o seu peso: '))
imc = peso/(alt*alt)
if imc<18.5:
    print(f'Valor do seu cálculo de IMC:{imc:.2f}')
    print('Seu IMC está abaixo de 18.5, você está abaixo do peso.')
elif imc>=18.5 and imc<25:
    print(f'Valor do seu cálculo de IMC:{imc:.2f}')
    print('Seu IMC está entre 18.5 e 25, você está no peso ideal.')
elif imc>=25 and imc<30:
    print(f'Valor do seu cálculo de IMC:{imc:.2f}')
    print('Seu IMC está entre 25 e 30, você está com sobrepeso.')
elif imc>=30 and imc<=40:
    print(f'Valor do seu cálculo de IMC:{imc:.2f}')
    print('Seu IMC está entre 30 e 40, você está com obesidade.')
else:
    print(f'Valor do seu cálculo de IMC:{imc:.2f}')
    print('Seu IMC está acima de 40, você está com obesidade mórbida.')    