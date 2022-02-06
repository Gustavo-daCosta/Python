from exc115.sistema import Menu, CadastrarPessoa, VerPessoasCadastradas

while True:
    opcao = Menu()
    if opcao == 1:
        CadastrarPessoa()
    elif opcao == 2:
        VerPessoasCadastradas()
    else:
        print('Finalizando...')
        break