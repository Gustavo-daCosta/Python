titulo = 'CÁLCULO DO IMC'
print('-'*40)
print(f'{titulo:^40}')
print('-'*40)
peso = float(input('Peso: '))
altura = float(input('Altura: '))
print('-'*40)
imc = peso / (altura*altura)
print(f'IMC: {imc:.1f}')
if imc < 18.5:
    print('Abaixo de 18.5: Abaixo do peso')
if imc >= 18.5 and imc <= 25:
    print('Entre 18.5 e 25: Peso ideal')
if imc > 25 and imc <= 30:
    print('Entre 25 e 30: Sobrepeso')
if imc > 30 and imc <= 40:
    print('Entre 30 e 40: Obesidade')
if imc > 40:
    print('Acima de 40: Obesidade mórbida')