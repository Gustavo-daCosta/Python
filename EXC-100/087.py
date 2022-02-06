def Gerador(mensagem):
    print(f'***{"-"*11}{"="*22}{"-"*11}***')
    print(f"{mensagem.center(50)}")
    print(f'***{"-"*11}{"="*22}{"-"*11}***')

titulo = str(input('Digite um título: '))
Gerador(titulo)