# Baixar SQLITE no https://sqlitestudio.pl/

import sqlite3
from sqlite3 import Error

#Caminho do banco de dados
q = "C:\\Py\\Db_agenda.db"

# Conexão
def Conexao_banco(query):
    connection = None
    try:
        connection = sqlite3.connect(query)
        print("="*80)
        print("Conexão executada com sucesso!!")
        print("=" * 80)
    except  Error as err:
        print("=" * 80)
        print('erro na conexão')
        print(f"Error: '{err}'")
        print("=" * 80)

    return connection
vcon = Conexao_banco(q)
# Criar Tabela
vsql = """ CREATE TABLE tb_contatos (
    n_idcontatos INTEGER      PRIMARY KEY AUTOINCREMENT,
    t_nome       VARCHAR (55) NOT NULL,
    t_telefone   VARCHAR (15) NOT NULL,
    t_email      VARCHAR (30)
);
"""

# função para criar tabela
def Criar_tabela(conexao,sql):
    try:

      c = conexao.cursor()
      c.execute(sql)
      print("=" * 80)
      print("Tabelas criadas com sucesso!")
      print("=" * 80)

    except Error as err:
        print("=" * 80)
        print('erro na criação da tabela')
        print(f"Error: '{err}'")
        print("=" * 80)


Criar_tabela(vcon,vsql)
vcon.close()