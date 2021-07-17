import sqlite3
from sqlite3 import Error

""" CRIAR CONEXÃO """
def ConexaoBanco():
    caminho = "D:\\Projetos\\projeto_agenda\\banco.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon = ConexaoBanco()

""" CRIAR TABELA """
vsql = """
        CREATE TABLE usuario_senha(        
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER VARCHAR(12),
        SENHA VARCHAR(8)        
        );
        """
def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela Criada")
    except Error as ex:
        print(ex)

criarTabela(vcon, vsql)

vcon.close()