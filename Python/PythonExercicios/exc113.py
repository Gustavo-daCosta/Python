def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        try:
            valor = int(n)
            ok = True
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar um número.')
            valor = 0
        except ValueError:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            ok = False
        if ok is True:
            break
    return valor

def leiaFloat(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        try:
            valor = float(n)
            ok = True
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar um número.')
            valor = 0
        except ValueError:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            ok = False
        if ok is True:
            break
    return valor

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real {real}')