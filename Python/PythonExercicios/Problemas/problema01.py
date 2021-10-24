# Problema #1 - Meu salário por hora
# Escreva um programa que retorne o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

while True:
    try:
        salario = float(input('Salário mensal: '))
        horas = int(input('Horas trabalhadas por mês: '))
    except:
        print('ERRO! Valor inválido digitado, tente novamente')
    finally:
        if isinstance(salario, float) is True and isinstance(horas, int) is True:
            break
    
valorHora = salario/horas
print(f'Valor/Hora do funcionário: R${valorHora:.2f}')