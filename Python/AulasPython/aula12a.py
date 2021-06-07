nome = str(input('Qual é o seu nome? ')).capitalize()
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Larah':
    print('Belo nome!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}.')
#NOTA: O else é opcional.