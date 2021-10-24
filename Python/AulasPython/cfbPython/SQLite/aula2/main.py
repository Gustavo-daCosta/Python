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

nome = str(input('Digite o nome: '))
telefone = str(input('Digite o telefone: '))
email = str(input('Digite o email: '))

vsql = f"""INSERT INTO tb_contatos 
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
        VALUES('{nome}', '{telefone}', '{email}')"""
def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido')
    except Error as ex:
        print(ex)

inserir(vcon, vsql)