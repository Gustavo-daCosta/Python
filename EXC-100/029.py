titulo = 'REAJUSTE DE SALÁRIOS'
print('-'*40)
print(f'{titulo:^40}')
print('-'*40)
nome = str(input('Nome do funcionário: '))
salario = float(input('Salário do funcionário: R$'))
anos = int(input('Anos de empresa: '))
if anos <= 3:
    reajuste = salario*0.3
    msg = 'Você tem direito a um aumento de 3% no salário!'
if anos > 3 and anos < 10:
    reajuste = (salario*0.25) / 2
    msg = 'Você tem direito a um aumento de 12,5% no salário!'
if anos >= 10:
    reajuste = salario * 0.20
    msg = 'Você tem direito a um aumento de 20% no salário!'
print('-'*40)
print(f'Parabéns {nome}! {msg}')
print(f'Valor do reajuste: R${reajuste:.2f}')
print(f'Valor do novo salário: R${salario+reajuste:.2f}')