from os import system, path

caminho = path.dirname(__file__)
nomeArquivo = caminho + '\\registro.txt'

def titulo(texto):
    print('-'*45)
    print(texto.center(45))
    print('-'*45)

def Menu():
    system('cls')
    titulo('MENU PRINCIPAL')
    print('''[ 1 ] - Cadastrar nova pessoa
[ 2 ] - Ver pessoas cadastradas
[ 3 ] - Sair do sistema''')
    while True:
        try:
            opcao = int(input('Selecione uma opção: '))
        except:
            print('ERRO! Digite uma opção válida')
        finally:
            if isinstance(opcao, int) is True and 0 < opcao < 4:
                break
            else:
                print('ERRO! Digite um valor entre 1 e 3.')
    return opcao

def CadastrarPessoa():
    # nome / idade / email
    system('cls')
    while True:
        titulo('Opção 1')
        try:
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
            email = str(input('E-mail: '))
        except:
            print('ERRO! Valor inválido, tente novamente.')
        finally:
            if '@' in email and '.' in email and len(email) <= 64:
                print('Registro concluído!')
                input('Aperte ENTER para continuar...')
                system('cls')
                break
    arquivo = open(nomeArquivo, "a")
    arquivo.write('\n')
    arquivo.write(f'Nome\t: {nome}\n')
    arquivo.write(f'Idade\t: {idade}\n')
    arquivo.write(f'E-mail\t: {email}\n')
    arquivo.write('-'*35)
    arquivo.close


def VerPessoasCadastradas():
    system('cls')
    titulo('Opção 2')
    arquivo = open(nomeArquivo, 'r')
    pessoasCadastradas = arquivo.read()
    print(pessoasCadastradas)
    input('Aperte ENTER para continuar...')