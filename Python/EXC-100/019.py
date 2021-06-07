print('=-=-=-=-= ANÁLISE DE APROVEITAMENTO =-=-=-=-=')
nome = str(input('Nome: '))
nota1 = float(input('1° Nota: '))
nota2 = float(input('2° Nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f'A média de {nome} é {media:.1f}')
    print(f'{nome} teve um bom aproveitamento!')
else:
    print(f'A média de {nome} é {media:.1f}')
    print(f'{nome} não teve um bom aproveitamento!')