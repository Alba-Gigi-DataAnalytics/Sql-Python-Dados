-- Exercicios_Semana.5 Bootcamp Data Analytics: Banco de Dados SQL  
-- Criar uma conexão com o banco de dados SQLite > apontador arquivo a ser utilizado.
-- (1). Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto)."""

CREATE TABLE IF NOT EXISTS tb_alunos(
							id_aluno INT NOT NULL PRIMARY KEY,
							nome VARCHAR(50) NOT NULL,
							idade INT NOT NULL,
							curso VARCHAR(50) NOT NULL);

-- (2). Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
-- Populando fazendo uso de uma List of Tuples

INSERT INTO tb_alunos(id_aluno, nome, idade, curso) VALUES 	(1, "Joao Nogueira", 22, "Engenharia"),
		(2, "Janete Silva", 35, "Fisica Nuclear"),
		(3, "Roberta Johnson", 19, "Matematica"),
		(4, "Sarah Barbosa", 21, "Engineering Computacao"),
		(5, "Michael Wilson", 23, "Computer Science");

-- MAIS registros fazendo List of Tuples, tabela tb_alunos (que ja tem 5 alunos).


INSERT INTO tb_alunos (id_aluno, nome, idade, curso) VALUES	(6, "André Oliveira", 24, "Ciência da Computação"),
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
		(25, "Patrícia Santos", 26, "Marketing");


-- (3). Consultas Básicas: escreva consultas SQL para realizar as seguintes tarefas:
-- Para realizar consultas simples SELECT sintaxe: SELECT campo1, campo2, campo3 FROM nome_tabela;

-- (3.a) Selecionar todos os registros da tabela "alunos".
SELECT * 
FROM tb_alunos;

SELECT id_aluno, nome, idade, curso
FROM tb_alunos;

-- (3.b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
SELECT nome, idade
FROM tb_alunos
WHERE idade > 20;

-- (3.c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
SELECT *
FROM tb_alunos
WHERE curso LIKE "Engenharia%"
ORDER BY nome;

-- (3.d) Contar o número total de alunos na tabela
SELECT COUNT(*)
FROM tb_alunos;

-- 4. UPDATE a escrita nome do curso "Engineering Computacao" mudar para "Engenharia da Computacao"
UPDATE tb_alunos
SET curso="Engenharia da Computacao"
WHERE curso="Engineering Computacao";

-- (4.a) UPDATE idade de um aluno específico na tabela.
UPDATE tb_alunos
SET idade = 34
WHERE id_aluno=14;

-- (REPETIR 3.C) Confirmar atualizou, SELECT alunos do curso de "Engenharia" em ordem alfabética.
SELECT *
FROM tb_alunos
WHERE curso LIKE "Engenharia%"
ORDER BY nome;

-- (4.b)DUPLICANDO PROPOSITALMENTE para DELETAR (registros de alunos [(tb_alunos)].
INSERT INTO tb_alunos(id_aluno, nome, idade, curso) VALUES (26, "Joao Nogueira", 22, "Engenharia"),
    (27, "Janete Silva", 35, "Fisica Nuclear"),
    (28, "Roberta Johnson", 19, "Matematica"),
    (29, "Sarah Barbosa", 21, "Engenharia da Computacao"),
    (30, "Michael Wilson", 23, "Computer Science");

-- (4.b) Remova um aluno pelo seu ID.
DELETE FROM tb_alunos
WHERE id_aluno = 11;

-- (4.b) APAGAR registros alunos [(tb_alunos)], CONDICAO .AND. instrução DELETE 
DELETE FROM tb_alunos
WHERE nome = "Sarah %" AND curso = "Engineering Computacao";

-- (5.a). Nova tabela CREATE [tb_clientes] + INSERT INTO registro ["id_cliente"]:
-- Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 
CREATE TABLE IF NOT EXISTS tb_clientes (
							id_cliente INT NOT NULL PRIMARY KEY,
							nome VARCHAR(50) NOT NULL,
							idade INT NOT NULL,
							saldo REAL NOT NULL);

-- (5.b) INSERT INTO "tb_clientes" Loop FOR com a variável i sendo usada para criar tipo AUTO_INCREMENT registros exclusivos [id_cliente]. 
INSERT INTO tb_clientes (id_cliente, nome, idade, saldo)
VALUES ("Ana Silva","Bruno Santos", "Camila Oliveira", "Diego Pereira", "Eduarda Lima", "Felipe Costa", "Gabriela Ferreira",
		"Hugo Souza", "Isabela Rodrigues", "João Almeida","Kátia Silva", "Lucas Santos", "Mariana Pereira",
		"Nathan Lima", "Olivia Ferreira", "Pedro Costa", "Quiteria Sousa", "Rafael Rodrigues", "Sofia Almeida", "Thiago Silva");

-- (5.c) UPDATE nome cliente específico na tabela
UPDATE tb_clientes,
SET nome = "Anna Silva",
WHERE id_cliente = 1;

-- (6.a) CONSULTAR, funções agregadas, consultas SQL e imprimir resultados.
--  Selecione o nome e a idade dos clientes com idade superior a 30 anos.
SELECT nome, idade 
FROM tb_clientes
WHERE idade > 30;

-- (6.b) AVG(saldo) Calcular o saldo médio dos clientes AVG(saldo)
SELECT AVG(saldo)
FROM tb_clientes;

-- (6.c) MAX(saldo) Encontrar tb_cliente que tenha o saldo máximo
SELECT * FROM tb_clientes
WHERE saldo = (SELECT MAX(saldo) FROM tb_clientes);

-- (6.d) SELECT COUNT(*) quantos clientes têm saldo acima de 1000
SELECT COUNT(*)
FROM tb_clientes
WHERE saldo > 1000;

-- (7) UPDATE e DELETE fazendo uso de CONDICIONAL 
-- (7.a) Atualize o saldo de um cliente específico

UPDATE tb_clientes
SET saldo = 1100.50
WHERE id_cliente=2;

-- (7.b) DELETE Remova um cliente pelo seu ID
DELETE FROM tb_clientes
WHERE id_cliente=7;

-- (8) JOIN Junção de Tabelas - CREATE TABLES [tb_compras] com o esquema especificado.
-- (8.a) Crie uma tabela chamada 'compras' 

CREATE TABLE IF NOT EXISTS tb_compras (id_compra INT NOT NULL PRIMARY KEY,
       							id_cliente INT NOT NULL,
								produto VARCHAR(150) NOT NULL,
								valor REAL NOT NULL,
        						FOREIGN KEY (id_cliente) REFERENCES tb_clientes(id_cliente));

-- (8.b) Inserir 20 compras > RANDOM produtos > valores aleatórios e associados > id_cliente (FK) existentes da tabela tb_clientes (PK).
-- Gerar dados aleatórios para 20 clientes (cliente, produto, valor)
INSERT INTO tb_compras(id_compra, id_cliente, produto, valor)
VALUES ("Notebook", "Smartphone", "TV", "Tablet", "Monitor","Processador", "HDSound", "SuperTV", "Mouse", "Teclado",
        "Impressora", "Câmera","Fone de Ouvido","Roteador","Console","Caixa de Som", "Máquina de Lavar", "Geladeira", "Fogão");

-- (8.c) Recuperar e exibir nome id_cliente, produto e valor > cada compra usando uma instrução SELECT operação JOIN.
--  Instrução SELECT recupera dados da tabela e busca registros usando método fetchall().
SELECT tb_clientes.nome, tb_compras.produto, tb_compras.valor
FROM tb_clientes
JOIN tb_compras ON tb_clientes.id_cliente = tb_compras.id_cliente;

