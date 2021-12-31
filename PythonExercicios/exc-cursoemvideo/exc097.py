def palavra(a):
    carac = (len(a) + 4)
    print('~' * carac)
    print(f'  {a}  ')
    print('~' * carac)

palavra(a = str(input('Título: ')))