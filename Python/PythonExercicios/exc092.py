from datetime import datetime
data = datetime.today()
ano = data.year
lista = dict()
lista['ctps'] = 1
while True:
    del lista['ctps']
    lista.update({'nome': str(input('Nome: ')),
        'nasc': int(input('Ano de nascimento: ')),
        'ctps': int(input('Carteira de trabalho (0 não tem): '))})
    if lista['ctps'] == 0:
        break
    lista.update({'contrat': int(input('Ano de contratação: ')),
        'salario': float(input('Salário: R$')),})
    lista['aposentadoria'] = ((ano - (lista.get('nasc'))) - (ano - (lista.get('contrat')))) + 35
    print(lista['aposentadoria'])
    break
print('=-='*25)
print(lista)
print(f'Nome tem o valor {lista["nome"]}')
print(f'Idade tem o valor {ano - (lista["nasc"])}')
print(f'ctps tem o valor {lista["ctps"]}')
if lista["ctps"] != 0:
    print(f'Contratação tem o valor {lista["contrat"]}')
    print(f'Salário tem o valor R${lista["salario"]:.2f}')
    print(f'Aposentadoria tem o valor {lista["aposentadoria"]}')