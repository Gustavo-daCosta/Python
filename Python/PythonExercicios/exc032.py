ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano {ano} é Bissexto!')
        else:
            print(f'O ano {ano} não é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')
else:
    print(f'O ano {ano} não é bissexto')