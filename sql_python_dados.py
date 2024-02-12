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
cursor.execute('SELECT id_aluno, nome, idade, curso FROM tb_alunos;')
dados_aluno = cursor.fetchall()
for aluno in dados_aluno:
    print(aluno)

# Para enviar e fechar conexao, evitando conflito com o sistema gerenciador 
# Commit the changes
conexao.commit()
# Close the connection
conexao.close()
