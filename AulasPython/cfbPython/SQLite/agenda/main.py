import sqlite3
from sqlite3 import Error
import os

# Conexão
def ConexaoBanco():
    caminho = "C:/Users/macie/OneDrive/Área de Trabalho/Python/Python/AulasPython/cfbPython/SQLite/database/agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = ConexaoBanco()


# Insert / Delet / Update
def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Operação realizada com sucesso!')

# Select
def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    # conexao.close()
    return res

def menuPrincipal():
    os.system('cls')
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registros")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")

def ErrorMessage(msg):
    os.system('cls')
    print(msg)
    os.system('pause')

def menuInserir():
    os.system('cls')
    nome = str(input("Digite o nome do contato: "))
    telefone = str(input("Digite o telefone do contato: "))
    email = str(input("Digite o email do contato: "))
    vsql = f"""INSERT INTO tb_contatos 
                (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
            VALUES('{nome}', '{telefone}', '{email}')"""
    query(vcon, vsql)

def menuDeletar():
    os.system('cls')
    vID = input("Digite o ID do registro a ser deletado: ")
    vsql = f"DELETE FROM tb_contatos WHERE N_IDCONTATO = {vID}"
    query(vcon, vsql)

def menuAtualizar():
    os.system('cls')
    vID = input("Digite o ID do registro a ser atualizado: ")
    r = consultar(vcon, f"SELECT * FROM tb_contatos WHERE N_IDCONTATO = {vID}")
    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]
    vnome = str(input(f"Digite o novo nome do contato {rnome}: "))
    vtelefone = str(input(f"Digite o novo telefone do contato {rtelefone}: "))
    vemail = str(input(f"Digite o novo email do contato {remail}: "))

    if len(vnome) == 0:
        vnome = rnome
    if len(vtelefone) == 0:
        vtelefone = rtelefone
    if len(vemail) == 0:
        vemail = remail

    vsql = f"""UPDATE tb_contatos SET T_NOMECONTATO = '{vnome}', T_TELEFONECONTATO = '{vtelefone}', T_EMAILCONTATO = '{vemail}' WHERE N_IDCONTATO = '{vID}'"""
    query(vcon, vsql)

def menuConsultar():
    os.system('cls')
    print('Lista de nomes')
    vsql = "SELECT * FROM tb_contatos"
    res = consultar(vcon, vsql)
    limitemax = 10
    cont = 0
    for r in res:
        print(f"ID: {r[0]: <3} Nome: {r[1]: <30} Telefone: {r[2]: <14} / Email: {r[3]:<30}")
        cont += 1
        if cont >= limitemax:
            cont = 0
            os.system("pause")
            os.system('cls')
    print('Fim da lista')
    os.system('pause')

def menuConsultarNomes():
    os.system('cls')
    nome = str(input('Digite o nome: '))
    vsql = f"SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%{nome}%'"
    res = consultar(vcon, vsql)
    limitemax = 10
    cont = 0
    for r in res:
        print(f"ID: {r[0]: <3} Nome: {r[1]: <30} Telefone: {r[2]: <14} / Email: {r[3]:<30}")
        cont += 1
        if cont >= limitemax:
            cont = 0
            os.system("pause")
            os.system('cls')
    print('Fim da lista')
    os.system('pause')

opcao = 0
while opcao != 6:
    menuPrincipal()
    try:
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            menuInserir()
        
        elif opcao == 2:
            menuDeletar()

        elif opcao == 3:
            menuAtualizar()
        
        elif opcao == 4:
            menuConsultar()
        
        elif opcao == 5:
            menuConsultarNomes()
        
        elif opcao == 6:
            # Sair
            os.system('cls')
            print("Programa finalizado!")
            vcon.close()
            break
        else:
            ErrorMessage("Opção inválida!")
    except ValueError:
        ErrorMessage("Erro! Tente novamente.")