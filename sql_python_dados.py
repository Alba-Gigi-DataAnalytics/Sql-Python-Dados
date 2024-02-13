### ESTRUTURA GERAL PARA FAZER A CONEXAO
# SCRIPT DE BANCO DE DADOS: arquivo (ou conjunto de comandos) que quando executados criam um BD.

# Import all libraries   
import sqlite3
import random

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

# MAIS registros fazendo List of Tuples, tabela tb_alunos (que ja tem 5 alunos).
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

# Instrução SELECT recuperar dados tabela, usando método fetchone().
total_alunos = cursor.fetchone()[0]
print(f'\nTotal de {total_alunos} alunos.')

# 4. UPDATE a escrita nome do curso "Engineering Computacao" mudar para "Engenharia da Computacao"
cursor.execute('UPDATE tb_alunos SET curso="Engenharia da Computacao" WHERE curso="Engineering Computacao";')
update_count = cursor.rowcount
print(f'Número de registros atualizados: {update_count}')

# (4.a) UPDATE idade de um aluno específico na tabela.
cursor.execute('UPDATE tb_alunos SET idade = 34 WHERE id_aluno=14;')

# (REPETIR 3.C) Confirmar atualizou, SELECT alunos do curso de "Engenharia" em ordem alfabética.
cursor.execute('SELECT * FROM tb_alunos WHERE curso LIKE "Engenharia%" ORDER BY nome;')
dados_engenheiro = cursor.fetchall()
for engenheiros in dados_engenheiro:
    print(engenheiros)

# (4.b)DUPLICANDO PROPOSITALMENTE para DELETAR (registros de alunos [(tb_alunos)].
five_students_data = [
    (26, "Joao Nogueira", 22, "Engenharia"),
    (27, "Janete Silva", 35, "Fisica Nuclear"),
    (28, "Roberta Johnson", 19, "Matematica"),
    (29, "Sarah Barbosa", 21, "Engenharia da Computacao"),
    (30, "Michael Wilson", 23, "Computer Science")
]
# Comando INSERT sintaxe: INSERT INTO nome_tabela("campo1", "campo2", ...) VALUES ("valor1", "valor2",...);
cursor.executemany('INSERT INTO tb_alunos(id_aluno, nome, idade, curso) VALUES (?, ?, ?, ?)', five_students_data)

# (4.b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM tb_alunos WHERE id_aluno = 11;')
# (4.b) APAGAR registros alunos [(tb_alunos)], instrução DELETE cláusula ROWID e EXISTS para manter apenas os
# registro MAIS recentes dentro conjuntos de dados DUPLICADOS (primeiro IDENTIFICA e depois DELETE).
cursor.execute('DELETE FROM tb_alunos WHERE nome = "Sarah %" AND curso = "Engineering Computacao";')
# (*) ROWID identifica exclusivamente cada linha DISTINCT tabela.
cursor.execute('DELETE FROM tb_alunos WHERE ROWID NOT IN (SELECT MAX(ROWID) FROM tb_alunos GROUP BY nome, idade, curso);')

# (5). Nova tabela CREATE [tb_clientes] + INSERT INTO registro ["id_cliente"]:
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 

# Executar a instrução SQL para criar a tabela "clientes".
cursor.execute('CREATE TABLE IF NOT EXISTS tb_clientes (id_cliente INT NOT NULL PRIMARY KEY, nome VARCHAR(50) NOT NULL, idade INT NOT NULL, saldo REAL NOT NULL);')

# (5.a) Define uma lista de nomes
full_names = ["Ana Silva", "Bruno Santos", "Camila Oliveira", "Diego Pereira", "Eduarda Lima", "Felipe Costa", "Gabriela Ferreira", "Hugo Souza", "Isabela Rodrigues", "João Almeida",
                   "Kátia Silva", "Lucas Santos", "Mariana Pereira", "Nathan Lima", "Olivia Ferreira", "Pedro Costa", "Quiteria Sousa", "Rafael Rodrigues", "Sofia Almeida", "Thiago Silva"]
# Gerar dados aleatórios para 20 clientes (nomes, idades e saldos)
insert_data = []
for i in range(1, 21):
    # Biblioteca RANDOM e method .choice() para popular table.
    nome = random.choice(full_names)
    idade = random.randint(20, 60)
    saldo = round(random.uniform(500.0, 2000.0), 2)
    insert_data.append((i, nome, idade, saldo))
# (5.b) INSERT INTO "tb_clientes" Loop FOR com a variável i sendo usada para criar tipo AUTO_INCREMENT registros exclusivos [id_cliente]. 
# Isso garante que cada linha na tabela tb_clientes terá um id_cliente distinto.
cursor.executemany('INSERT INTO tb_clientes (id_cliente, nome, idade, saldo) VALUES (?, ?, ?, ?);', insert_data)

# (5.c) UPDATE nome cliente específico na tabela.
cursor.execute('UPDATE tb_clientes SET nome = "Anna Silva" WHERE id_cliente = 1;')

# (6.a) CONSULTAR, funções agregadas, consultas SQL e imprimir resultados.
# Selecione o nome e a idade dos clientes com idade superior a 30 anos.
cursor.execute("SELECT nome, idade FROM tb_clientes WHERE idade > 30;")
result_a = cursor.fetchall()
print("Result (a):", result_a)

# (6.b) Calcular o saldo médio dos clientes AVG(saldo)
cursor.execute("SELECT AVG(saldo) FROM tb_clientes;")
result_b = cursor.fetchone()[0]
print("Result (b):", result_b)

# (6.c) Encontrar tb_cliente que tenha o saldo máximo MAX(saldo).
cursor.execute("SELECT * FROM tb_clientes WHERE saldo = (SELECT MAX(saldo) FROM tb_clientes);")
result_c = cursor.fetchall()
print("Result (c):", result_c)

# (6.d) SELECT COUNT(*) quantos clientes têm saldo acima de 1000
cursor.execute("SELECT COUNT(*) FROM tb_clientes WHERE saldo > 1000;")
result_d = cursor.fetchone()[0]
print("Result (d):", result_d)

# 7. UPDATE e DELETE fazendo uso de CONDICIONAL 
# (7.a) Atualize o saldo de um cliente específico.
cursor.execute("UPDATE tb_clientes SET saldo = 1100.50 WHERE id_cliente=2;")
update_count = cursor.rowcount
print(f'Número de registros atualizados: {update_count}')

# (7.b) Remova um cliente pelo seu ID.
cursor.execute("DELETE FROM tb_clientes WHERE id_cliente=7;")

# 8. Junção de Tabelas - CREATE TABLES [tb_compras] com o esquema especificado.
# (8.a) Crie uma tabela chamada 'compras' 
# tb_compras: id (primary key), id_cliente (foreign key references id tb_cliente), produto (text),  valor (real).
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tb_compras (
        id_compra INTEGER NOT NULL PRIMARY KEY,
        id_cliente INTEGER NOT NULL,
        produto VARCHAR(150) NOT NULL,
        valor REAL NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES tb_clientes(id_cliente)
    );
''')

# (8.b) Inserir 20 compras > RANDOM produtos > valores aleatórios e associados > id_cliente (FK) existentes da tabela tb_clientes (PK).
produtos_data = [
    "Notebook", "Smartphone", "TV", "Tablet", "Monitor",
    "Processador", "HDSound", "SuperTV", "Mouse", "Teclado",
    "Impressora", "Câmera", "Fone de Ouvido", "Roteador", "Console",
    "Caixa de Som", "Máquina de Lavar", "Geladeira", "Fogão"
]
for i in range(1, 21):
    id_cliente = random.randint(1, 20)
    produto = random.choice(produto_data)
    valor = round(random.uniform(100.0, 2000.0), 2)
    produtos_data.append((i, id_cliente, produto, valor))
# Insert the purchases into the "purchases" table
    cursor.execute('INSERT INTO tb_compras(id_cliente, produto, valor) VALUES (?, ?, ?)', (id_cliente, produto, valor))

# (8.c) Recuperar e exibir nome id_cliente, produto e valor > cada compra usando uma instrução SELECT operação JOIN.
# Instrução SELECT recupera dados da tabela e busca registros usando método fetchall().
cursor.execute('''
    SELECT tb_clientes.nome, tb_compras.produto, tb_compras.valor
    FROM tb_clientes
    JOIN tb_compras ON tb_clientes.id_cliente = tb_compras.id_cliente;
''')
compras_info = cursor.fetchall()
for purchase in compras_info:
    print(f"Cliente: {purchase[0]}, Produto: {purchase[1]}, Valor: R${purchase[1]:.2f}")

# Enviar e fechar conexao, evitando conflito com o sistema gerenciador 
# Commit changes
connection.commit()
# Close connection
connection.close()