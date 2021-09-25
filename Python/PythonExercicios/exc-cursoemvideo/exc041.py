from datetime import date
atual = date.today().year
print('='*45)
print('     CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('='*45)
nasc = int(input('Ano de nascimento do atleta: '))
idade = atual - nasc
if idade<=9:
    print(f'Classificação atual: Atleta MIRIM.')
elif idade<=14:
    print(f'Classificação atual: Atleta INFANTIL.')
elif idade<=19:
    print(f'Classificação atual: Atleta JUNIOR.')
elif idade==20:
    print(f'Classificação atual: Atleta SÊNIOR.')
else:
    print(f'Classificação atual: Atleta MASTER.')