def Gerador(mensagem: str, ocorrencias: int):
    print(f'***{"-"*11}{"="*22}{"-"*11}***')
    for c in range(0, ocorrencias):
        print(f"{mensagem.center(50)}")
    print(f'***{"-"*11}{"="*22}{"-"*11}***')

titulo = str(input('Digite um título: '))
ocorrencias = int(input("Digite o número de ocorrências da mensagem: "))
Gerador(titulo, ocorrencias)