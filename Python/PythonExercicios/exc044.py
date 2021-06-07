print('=-='*20)
print('         MERCADO PYTHON')
print('=-='*20)
valor = float(input('Digite o preço das compras: R$'))
print('''Formas de pagamento:
[ 1 ] à vista - dinheiro/cheque
[ 2 ] à vista - cartão
[ 3 ] 2x - cartão
[ 4 ] 3x ou mais - cartão''')
opcao = int(input('Digite sua opção: '))
if opcao==1:
    print('Você tem direito a um desconto de 10%!')
    dif = valor*0.10
    total = valor-dif
    print(f'Valor do desconto: R${dif}')
elif opcao==2:
    print('Você tem direito a um desconto de 5%!')
    dif = valor*0.05
    total = valor-dif
    print(f'Valor do desconto: R${dif}')
elif opcao==3:
    print('Você não tem direito a nenhum desconto.')
    dif = 0
    total = valor
    print(f'Sua compra será parcelada em 2x de R${(valor/2):.2f}')
elif opcao==4:
    parc = int(input('Deseja pagar em quantas parcelas? '))
    print('Sua compra receberá juros de 20%')
    dif = valor*0.20
    total = valor+dif
    print(f'Sua compra será parcelada em {parc}x de R${(total/parc):.2f}')
else:
    print('OPÇÃO INVÁLIDA! Tente novamente.')
print(f'O valor total a se pagar é de R${total}')