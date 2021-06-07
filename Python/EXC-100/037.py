print('-'*50)
print('REAJUSTE SALARIAL'.center(50))
print('-'*50)
salario = float(input('Salário atual: R$'))
while True:
    genero = str(input('Gênero: [M/F]: '))
    if genero in 'MmFf':
        break
    else:
        print(f'ERRO! Digite F para Feminino e M para Masculino.')
anos = int(input('Anos de empresa: '))
if genero in 'Ff':
    if anos < 15:
        dif = salario*0.05
    elif anos >= 15 and anos <= 20:
        dif = salario*0.12
    else:
        dif = dif = salario*0.20
else:
    if anos < 20:
        dif = salario*0.03
    elif anos >= 20 and anos <= 30:
        dif = salario*0.13
    else:
        dif = salario*0.25
print('-'*50)
print(f'Aumento do salário: R${dif:.2f}')
print(f'Novo salário: R${salario+dif:.2f}')