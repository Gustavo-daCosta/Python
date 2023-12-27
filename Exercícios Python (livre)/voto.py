from multiprocessing.sharedctypes import Value
from os import system

system('cls')
while True:
    print("=-="*12)
    print("POSSO VOTAR?".center(36))
    print("=-="*12)
    while True:
        try:
            idade = int(input("Digite a sua idade: "))
            if idade > 130 or idade < 0:
                raise ValueError
            else:
                system('cls')
                break
        except (ValueError, TypeError):
            print("ERRO! Por favor digite uma idade válida")
     
    if idade < 16:
        situacao = "Idade insuficiente para votar"
    elif idade < 18 or idade >= 60:
        situacao = "Voto opcional"
    else:
        situacao = "Voto obrigatório"
    print(f"Situação: {situacao}")
    print("=-="*12)

    while True:
        try:
            opcao = str(input("Deseja continuar? [S/N] ")).upper()
            if opcao in "NÃO" or opcao in "NAO":
                print("Saindo...")
                exit()
            elif opcao in "SIM":
                system('cls')
                break
            else:
                raise ValueError
        except (ValueError, TypeError):
            print("ERRO! Opção inválida, responda com 'Sim' ou 'Não'.")
