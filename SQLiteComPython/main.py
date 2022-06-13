# Removen o arquivo com o banco de dados SQLite
import os
os.remove("escola.db") if os.path.exists("escola.db") else None

import sqlite3

# criando conexao com o db
con = sqlite3.connect('escola.db')

# criando o cursor
cur = con.cursor()

# instrução sql para criar tabela
sql_create = '''create table cursos (
id integer primary key,
titulo varchar (100),
categoria varchar (100)
)'''

# executando a instrução
cur.execute(sql_create)

# criando instrução para inserir registros
sql_insert = 'insert into cursos values (?,?,?)'

# dados a serem  inseridos
recset = [(1000, 'Ciência de Dados', 'Data Science'),
          (1001, 'Big Data Fundamentos', 'Big Data'),
          (1002, 'Python Fundamentos', 'Análise de Dados')]

# inserindo os dados dando loop for na instrução
for i in recset:
    cur.execute(sql_insert, i)

# commitando a transação
con.commit()

# selecionando toda a tabela cursos
sql_select = 'select * from cursos'
cur.execute(sql_select)

# dando print nos dados
dados = cur.fetchall()
for i in dados:
    print(f'''Curso: {i[0]}, Título: {i[1]}, Categoria: {i[2]}''')

# fechando conexão
con.close()