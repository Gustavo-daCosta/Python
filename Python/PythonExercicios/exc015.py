dias = int(input('O carro foi alugado por quantos dias? '))
km = int(input('O carro rodou quantos km? '))
valor = (dias * 60) + (km * 0.15)
print(f'Valor total a se pagar é R${valor}')