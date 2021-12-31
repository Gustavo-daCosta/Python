print('=-=-=-= CÁLCULO DE REDUÇÃO DE VIDA =-=-=-=')
dia = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Você fuma a quantos anos? '))
total = (((anos * 365)* dia)* 10) / 24
print(f'Dias perdidos: {total}')