n = float(input('Digite o salário: R$'))
if n > 1250:
    s = n + (n * 0.10)
    print('Você tem direito a um aumento de 10%')
    print(f'Valor do aumento: R${n*0.10:.2f}')
    print(f'Seu novo salário com reajuste: R${s:.2f}')
else:
    s = n + (n * 0.15)
    print('Você tem direito a um aumento de 15%')
    print(f'Valor do aumento: R${n*0.15:.2f}')
    print(f'Seu novo salário com reajuste: R${s:.2f}')