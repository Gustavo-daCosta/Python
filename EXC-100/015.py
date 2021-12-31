titulo = 'DEFINIÇÃO DE SALÁRIO'
print('=-='*30)
print(f'{titulo:^90}')
print('=-='*30)
dias = int(input('Quantidade de dias trabalhados: '))
salario = (dias*8)*25
print(f'Salário: R${salario:.2f}')