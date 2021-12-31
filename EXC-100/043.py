for c in range(30, 0, -1):
    if c % 4 == 0:
        print(f'[{c}]', end=' ')
    else:
        print(c, end=' ')
print('Acabou!')