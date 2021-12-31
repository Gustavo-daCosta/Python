titulo = 'EMPRÉSTIMO BANCÁRIO'
print('-'*50)
print(f'{titulo:^50}')
print('-'*50)
casa = int(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Anos de pagamento: '))
prestacao = casa / (anos * 12)
print(f'30% do salário: R${salario*0.30:.2f}        Prestação mensal: R${prestacao:.2f}')
if prestacao > (salario * 0.30):
    print(f'A prestação mensal excede 30% do seu salário!')
    print('Seu empréstimo foi negado.')
else:
    print(f'A prestação mensal não excede 30% do seu salário!')
    print('Seu empréstimo foi aprovado.')