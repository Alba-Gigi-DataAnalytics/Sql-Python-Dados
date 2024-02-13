/* ### ESTRUTURA GERAL PARA FAZER A CONEXAO
# SCRIPT DE BANCO DE DADOS: arquivo (ou conjunto de comandos) que quando executados criam um BD.

# Import all libraries   
import sqlite3
import random

# Criar uma conexão com o banco de dados SQLite > apontador arquivo a ser utilizado.
conexao = sqlite3.connect('sql_python_dados')
# Criar um objeto cursor, para passar as informacoes de conexao
cursor = conexao.cursor()

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
# cursor.executemany('INSERT INTO tb_alunos(id_aluno, nome, idade, curso) VALUES (?, ?, ?, ?)', five_students_data)

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

# Instrução SELECT recupera dados da tabela e buscar todos os registros usando método fetchall().
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

# Instrução SELECT recuperar dados da tabela e buscar apenas um registro usando método fetchone().
total_alunos = cursor.fetchone()[0]
print(f'\nTotal de {total_alunos} alunos.')

# (4.a) Atualizar o curso "Engineering Computacao" para "Engenharia da Computacao"
cursor.execute('UPDATE tb_alunos SET curso="Engenharia da Computacao" WHERE curso="Engineering Computacao";')
update_count = cursor.rowcount
print(f'Número de registros atualizados: {update_count}')

# (REPETIR 3.C) Teremos mais alunso ao selecionar curso de "Engenharia".
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
cursor.executemany('INSERT INTO tb_alunos(id_aluno, nome, idade, curso) VALUES (?, ?, ?, ?)', five_students_data)

# (4.b) APAGAR registros de alunos [(tb_alunos)], instrução DELETE cláusula ROWID e EXISTS para manter apenas os
# registro MAIS recentes dentro conjuntos de dados DUPLICADOS (primeiro identificar e depois excluir).
# (*) ROWID é usado para identificar exclusivamente cada linha da tabela. Cada linha da tabela tem um ROWID distinto.
cursor.execute('DELETE FROM tb_alunos WHERE nome = "Sarah Barbosa";')
cursor.execute('DELETE FROM tb_alunos WHERE ROWID NOT IN (SELECT MAX(ROWID) FROM tb_alunos GROUP BY nome, idade, curso);')

# (4.b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM tb_alunos WHERE id_aluno = 11;')

# (5). Nova tabela CREATE [tb_clientes] + INSERT INTO registro ["id_cliente"]:
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 
# Executar a instrução SQL para criar a tabela "clientes".
cursor.execute('CREATE TABLE IF NOT EXISTS tb_clientes (id_cliente INT NOT NULL PRIMARY KEY, nome VARCHAR(50) NOT NULL, idade INT NOT NULL, saldo REAL NOT NULL);')

# (5.a) Define uma lista de nomes
brazilian_names = ["Ana", "Bruno", "Camila", "Diego", "Eduarda", "Felipe", "Gabriela", "Hugo", "Isabela", "João",
                   "Kátia", "Lucas", "Mariana", "Nathan", "Olivia", "Pedro", "Quiteria", "Rafael", "Sofia", "Thiago"]
# Gerar dados aleatórios para 20 clientes (nomes, idades e saldos)
insert_data = []
for i in range(1, 21):
    # Biblioteca com method para popular table: random.choice().
    name = random.choice(brazilian_names)
    age = random.randint(20, 60)
    balance = round(random.uniform(500.0, 2000.0), 2)
    insert_data.append((i, name, age, balance))
    
# (5.b) Criar e executar o comando INSERT na tabela "clientes".
# Loop FOR gera dados aleatórios (5.b), variável i é usada para criar registros exclusivos [id_cliente]. 
# Isso garante que cada linha na tabela tb_clientes terá um id_cliente distinto.
cursor.executemany('INSERT INTO tb_clientes (id_cliente, nome, idade, saldo) VALUES (?, ?, ?, ?);', insert_data)

# Enviar e fechar conexao, evitando conflito com o sistema gerenciador 
# Commit changes
connection.commit()
# Close connection
connection.close()
**/









