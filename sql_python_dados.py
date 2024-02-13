### ESTRUTURA GERAL PARA FAZER A CONEXAO
# SCRIPT DE BANCO DE DADOS: arquivo (ou conjunto de comandos) que quando executados criam um BD.

# Import all libraries   
import sqlite3
# Criar uma conexão com o banco de dados SQLite > apontador arquivo a ser utilizado.
connection = sqlite3.connect('sql_python_dados')  # Replace 'your_database.db' with your actual database file
# Criar um objeto cursor, para passar as informacoes de conexao
cursor = connection.cursor()

# Exercicios_Semana.5 Bootcamp Data Analytics: Banco de Dados SQL  
# (1). Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto)."""
cursor.execute('CREATE TABLE IF NOT EXISTS tb_alunos(id_aluno INT NOT NULL PRIMARY KEY, nome VARCHAR(50) NOT NULL, idade INT NOT NULL, curso VARCHAR(50) NOT NULL);')

# (2). Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
# Populando fazendo uso de uma List of Tuples
five_students_data = [
    (1, "Joao Nogueira", 22, "Engenharia"),
    (2, "Janete Silva", 35, "Fisica Nuclear"),
    (3, "Roberta Johnson", 19, "Matematica"),
    (4, "Sarah Barbosa", 21, "Engineering Computacao"),
    (5, "Michael Wilson", 23, "Computer Science")
]

# Comando INSERT sintaxe: INSERT INTO nome_tabela("campo1", "campo2", ...) VALUES ("valor1", "valor2",...);
cursor.executemany('INSERT INTO tb_alunos(id_aluno, nome, idade, curso) VALUES (?, ?, ?, ?)', five_students_data)

# Inserindo registros fazendo uso de uma List of Tuples, tabela tb_alunos (que ja tem 5 alunos).
more_students_data = [
    (6, "André Oliveira", 24, "Ciência da Computação"),
    (7, "Mariana Santos", 28, "Engenharia Elétrica"),
    (8, "Fábio Costa", 26, "Administração"),
    (9, "Camila Lima", 22, "Medicina"),
    (10, "Rafael Pereira", 23, "Arquitetura"),
    (11, "Isabela Souza", 20, "Psicologia"),
    (12, "Lucas Rodrigues", 27, "Economia"),
    (13, "Aline Oliveira", 25, "Direito"),
    (14, "Bruno Mendes", 30, "Design Gráfico"),
    (15, "Carolina Silva", 29, "Engenharia Civil"),
    (16, "Gustavo Santos", 22, "Biologia"),
    (17, "Tatiane Costa", 26, "História"),
    (18, "Vinícius Lima", 24, "Comunicação Social"),
    (19, "Ana Paula Pereira", 31, "Química"),
    (20, "Felipe Mendonça", 28, "Filosofia"),
    (21, "Daniela Oliveira", 25, "Geografia"),
    (22, "Ricardo Silva", 27, "Engenharia Mecânica"),
    (23, "Jéssica Costa", 23, "Enfermagem"),
    (24, "Eduardo Lima", 29, "Nutrição"),
    (25, "Patrícia Santos", 26, "Marketing")
]
# Comando INSERT sintaxe: INSERT INTO nome_tabela("campo1", "campo2", ...) VALUES ("valor1", "valor2",...);
cursor.executemany('INSERT INTO tb_alunos (id_aluno, nome, idade, curso) VALUES (?, ?, ?, ?)', more_students_data)

# Para visualizar no terminal, precisamos chamar o print()
## Primeiro, criamos uma variável, depois associamos a seleção desejada
# (3). Consultas Básicas: escreva consultas SQL para realizar as seguintes tarefas:
## Para realizar consultas simples SELECT sintaxe: SELECT campo1, campo2, campo3 FROM nome_tabela;

# (3.a) Selecionar todos os registros da tabela "alunos".
cursor.execute('SELECT * FROM tb_alunos;')
cursor.execute('SELECT id_aluno, nome, idade, curso FROM tb_alunos;')
dados_aluno = cursor.fetchall()
for aluno in dados_aluno:
    print(aluno)

# (3.b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
cursor.execute('SELECT nome, idade FROM tb_alunos WHERE idade > 20;')
dados_maiores_vinte = cursor.fetchall()
for maiores in dados_maiores_vinte:
    print(maiores)

# (3.c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
cursor.execute('SELECT * FROM tb_alunos WHERE curso LIKE "Engenharia%" ORDER BY nome;')
dados_engenheiro = cursor.fetchall()
for engenheiros in dados_engenheiro:
    print(engenheiros)

# (3.d) Contar o número total de alunos na tabela
cursor.execute('SELECT COUNT(*) FROM tb_alunos;')
total_alunos = cursor.fetchone()[0]
print(f'\nTotal de {total_alunos} alunos.')

# (4.a) Atualizar o curso "Engineering Computacao" para "Engenharia da Computacao"
cursor.execute('UPDATE tb_alunos SET curso="Engenharia da Computacao" WHERE curso="Engineering Computacao";')
update_count = cursor.rowcount
print(f'Número de registros atualizados: {update_count}')

# (REPETIR 3.C) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
cursor.execute('SELECT * FROM tb_alunos WHERE curso LIKE "Engenharia%" ORDER BY nome;')
dados_engenheiro = cursor.fetchall()
for engenheiros in dados_engenheiro:
    print(engenheiros)

# (4.b)DUPLICANDO PROPOSITALMENTE para DELETAR (registros de alunos [(tb_alunos)].
five_students_data = [
    (26, "Joao Nogueira", 22, "Engenharia"),
    (27, "Janete Silva", 35, "Fisica Nuclear"),
    (28, "Roberta Johnson", 19, "Matematica"),
    (29, "Sarah Barbosa", 21, "Engineering Computacao"),
    (30, "Michael Wilson", 23, "Computer Science")
]
# Comando INSERT sintaxe: INSERT INTO nome_tabela("campo1", "campo2", ...) VALUES ("valor1", "valor2",...);
cursor.executemany('INSERT INTO tb_alunos(id_aluno, nome, idade, curso) VALUES (?, ?, ?, ?)', five_students_data)

# (4.b) APAGAR registros de alunos [(tb_alunos)], instrução DELETE 
# Registro MAIS recentes no conjuntos dados DUPLICADOS (primeiro identificar e depois excluir).
# SIMPLES uso do DELETE (registros de alunos [(tb_alunos)]
cursor.execute('DELETE FROM tb_alunos WHERE nome = "Sarah Barbosa";')

# SUBCONJUNTO usando cláusula ROWID e EXISTS para identificar exclusivamente cada linha da tabela. 
# Cada linha da tabela tem um ROWID distinto.
cursor.execute('DELETE FROM tb_alunos WHERE ROWID NOT IN (SELECT MAX(ROWID) FROM tb_alunos GROUP BY nome, idade, curso);')

# Para enviar e fechar conexao, evitando conflito com o sistema gerenciador 
# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()