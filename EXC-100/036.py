print('-'*50)
print('PROGRAMA VIDA SAUDÁVEL'.center(50))
print('-'*50)
horas = int(input('Total de horas de atividades físicas praticadas no mês: '))
if horas <= 10:
    pontos = horas*2
elif horas > 10 and horas <= 20:
    pontos = horas*5
else:
    pontos = horas*10
print('-'*50)
print(f'Total de pontos: {pontos}')
print(f'Valor ganho: R${pontos*0.05:.2f}')