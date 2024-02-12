### ESTRUTURA GERAL PARA FAZER A CONEXAO
# SCRIPT DE BANCO DE DADOS: arquivo (ou conjunto de comandos) que quando executados criam um BD.

# import all libraries   
import sqlite3
# Criar uma conexão com o banco de dados SQLite > apontador arquivo a ser utilizado.
conexao = sqlite3.connect('sql_python_dados')
# Criar um objeto cursor, para passar as informacoes de conexao
cursor = conexao.cursor()

# Exercicios_Semana.5 Bootcamp Data Analytics: Banco de Dados SQL  
# (1). Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto)."""
# cursor.execute('CREATE TABLE IF NOT EXISTS tb_alunos(id_aluno INT NOT NULL PRIMARY KEY, nome VARCHAR(50) NOT NULL, idade INT NOT NULL, curso VARCHAR(50) NOT NULL);')

# (2). Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
# Populando fazendo uso de uma List of Tuples
five_students_data = [
    (1, "Joao Nogueira", 22, "Engenharia"),
    (2, "Janete Silva", 35, "Fisica Nuclear"),
    (3, "Roberta Johnson", 19, "Matematica"),
    (4, "Sarah Barbosa", 21, "Engineering Computacao"),
    (5, "Michael Wilson", 23, "Computer Science")
]

# Para enviar e fechar conexao, evitando conflito com o sistema gerenciador 
# Commit the changes
conexao.commit()
# Close the connection
conexao.close()

