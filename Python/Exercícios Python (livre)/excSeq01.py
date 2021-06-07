titulo = 'CONTROLE DE RENDIMENTO'
print('=-='*15)
print(f'{titulo:^45}')
print('=-='*15)
peso = float(input('Digite quantos Kg de peixes foram pescados: '))
if peso <= 50:
    print('A quantidade de peixes não excede o limite, você não será multado.')
else:
    print('A quantidade de peixes excedeu o limite, você será multado.')
    excesso = peso - 50
    print(f'Excesso de peixes: {excesso}Kg')
    multa = excesso*4
    print(f'Valor da multa: R${multa:.2f}')