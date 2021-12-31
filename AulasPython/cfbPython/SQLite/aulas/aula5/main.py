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

# INSERIR
def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Registro inserido')
'''
nome = str(input('Digite o nome: '))
telefone = str(input('Digite o telefone: '))
email = str(input('Digite o email: '))

vsql = f"""INSERT INTO tb_contatos 
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
        VALUES('{nome}', '{telefone}', '{email}')"""

inserir(vcon, vsql)
'''

# DELETAR
def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Registro removido')

vsql = """DELETE FROM tb_contatos WHERE N_IDCONTATO = 2"""

#deletar(vcon, vsql)

# ATUALIZAR
def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Registro atualizado')

vsql = "UPDATE tb_contatos SET T_NOMECONTATO = 'Marcos', T_TELEFONECONTATO='(31)95976-4255', T_EMAILCONTATO='bruno@email.com.br' WHERE N_IDCONTATO = 2"
#atualizar(vcon, vsql)

# CONSULTAR
def consulta(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado

vsql = "SELECT * FROM tb_contatos"
vsql = "SELECT * FROM tb_contatos WHERE N_IDCONTATO = 3"
vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO = 'Marcos'"
vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE 'Marcos'" 
vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%o%'"
vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%o%' AND T_TELEFONECONTATO LIKE 'B%'"
vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%o%' OR T_TELEFONECONTATO LIKE '%no'"
resposta = consulta(vcon, vsql)

for r in resposta:
    print(r)
