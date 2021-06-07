nome = str(input('Nome: '))
while True:
    genero = str(input('Gênero: [M/F]: '))
    if genero in 'MFmf':
        break
    else:
        print('ERRO! Digite M (Masculino) ou F (Feminino) para continuar.')
valor = float(input('Valor das compras: R$'))
if genero == 'F':
    desconto = valor*0.13
    print(f'Mulheres tem direito a 13% de desconto.')
else:
    desconto = valor*0.05
    print(f'Homens tem direito a 5% de desconto.')
print(f'Valor do desconto: R${desconto:.2f}         Valor total a pagar: R${valor-desconto:.2f}')