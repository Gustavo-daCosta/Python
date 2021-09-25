dados = dict()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["media"]}')
if dados['media'] >= 7.0:
    print('Situação é igual a Aprovado')
elif dados['media'] < 7.0 and dados['media'] >= 5.0:
    print('Situação igual a Recuperação')
else:
    print('Situação igual a Reprovado')