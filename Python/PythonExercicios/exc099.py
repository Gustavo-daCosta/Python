from time import sleep

def maior(* num):
    print('=-='*20)
    print('Analisando os valores passados...')
    for c in num:
        print(c, end=' ', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) >  0:
        print(f'O maior valor informado foi {max(num)}')
    else:
        print(f'O maior valor informado foi {len(num)}')
maior(9, 2, 11, 5, 3)
maior(4, 7, 1, 2)
maior(1, 2, 3, 7, 3, 9, 5, 12)
maior(6)
maior(1, 2)
maior()