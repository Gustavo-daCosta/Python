from exc115.interface import cabecalho

lista = [
    'Ana Paula Vieira', 32,
    'Claúdio Mendonça', 18,
    'Gustavo Guanabara', 41,
    'Maria Clara Peixoto', 65,
    'Maurício Souza', 19,
    'Nilce Pedrosa', 43,
    'Pedro Gonçalves', 18,
    'Rafael Albuquerque', 38,
    'Renata Soares', 13
]

def cadastro():
    while True:
        print('-'*50)
        print('MENU PRINCIPAL'.center(50))
        print('-'*50)
        print('\033[1;33m1 -\033[m \033[1;34mVer pessoas cadastradas')
        print('\033[1;33m2 -\033[m \033[1;34mCadastrar nova pessoa')
        print('\033[1;33m3 -\033[m \033[1;34mSair do sistema')
        print('-'*50)
        try:
            opcao = int(input('\033[1;33mSua opção: \033[m'))
        except TypeError:
            print('ERRO')
        if opcao == 1:
            print('PESSOAS CADASTRADAS'.center(50))
            print('-'*50)
            for c in range(0, len(lista), 2):
                print(f'{lista[c]:<20}{lista[c+1]:>25} anos')
        elif opcao == 2:
            print('-'*50)
            print('NOVO CADASTRO'.center(50))
            print('-'*50)
            nome = str(input('Nome: '))
            lista.append(nome)
            lista.append(int(input('Idade: ')))
            print(f'Novo registro de {nome} adicionado.')
        else:
            break