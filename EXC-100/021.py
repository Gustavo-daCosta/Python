print('=-=-=-=-= ANO BISSEXTO =-=-=-=-=')
ano = int(input('Digite o ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'O ano de {ano} é Bissexto e tem 366 dias.')
else:
    print(f'O ano de {ano} não é Bissexto e tem 365 dias.')