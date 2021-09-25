nome, preco, opcao, total, mais1000, barato_nome, barato_preco, cont = 0, 0, 0, 0, 0, 0, 0, 1
produto = f'{cont}° PRODUTO'
while True:
    produto = f'{cont}° PRODUTO'
    print(f'{produto:-^50}')
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$'))
    total += preco
    if preco > 1000:
        mais1000 += 1
    if cont == 1:
        barato_preco = preco
        barato_nome = nome
    cont += 1
    if preco < barato_preco:
        barato_preco = preco
        barato_nome = nome
    print('-'*50)
    opcao = str(input('Você deseja continuar? [S/N]: ')).upper()
    if opcao == 'N':
        break
        print('======= FINALIZANDO =======')
print(f'Total de produtos registrados: {cont} produtos')
print(f'Total gasto na compra: R${total:.2f}')
print(f'Total de produtos com valor superior a R$1.000: {mais1000}')
print(f'''Nome e valor do produto mais barato:
Nome: {barato_nome}        Preço: R${barato_preco:.2f}''')