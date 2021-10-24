import sqlite3
from sqlite3 import Error


# Exemplo de como conectar com o banco de dados
def ConexaoBanco():
    caminho = "C:/Users/macie/OneDrive/Área de Trabalho/Python/Python/AulasPython/cfbPython/SQLite/database/agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = ConexaoBanco()

# Criar tabela
vsql="""CREATE TABLE tb_contatos(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
        );"""

def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela criada')
    except Error as ex:
        print(ex)

criarTabela(vcon, vsql)

vcon.close()