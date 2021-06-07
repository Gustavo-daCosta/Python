salario = float(input('Salário: R$'))
print('Você tem direito a um aumento de 15% no salário.')
print(f'Aumento: R${salario*0.15:.2f}     Salário com reajuste: R${(salario*0.15) + salario:.2f}')