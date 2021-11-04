import sqlite3 as conector

try:
    conexao = conector.connect("dev-python-noite.sqlite")

    cursor = conexao.cursor()

    sql_query = '''SELECT nome, matricula FROM Aluno;'''
    cursor.execute(sql_query)
    alunos = cursor.fetchall()
    for nome, matricula in alunos:
        print(f"Nome: {nome}, Matricula: {matricula}")

    # sql_insert_pessoa_trad = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
    #                             VALUES (12345678900, 'João', '2000-01-31', 1);'''
    # cursor.execute(sql_insert_pessoa_trad)
    cpf = int(input("Informe CPF: "))
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe data de nascimento: ")
    oculos = int(input("Usa oculos? 1-sim / 2-nao "))
    sql_insert_pessoa_din = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                                    VALUES (:cpf, :nome, :nascimento, :oculos);'''
    # cursor.execute(sql_insert_pessoa_din, (cpf, nome, data_nascimento, oculos))
    cursor.execute(sql_insert_pessoa_din, {"cpf": cpf,
                                           "nome": nome,
                                           "nascimento": data_nascimento,
                                           "oculos": oculos})
    conexao.commit()

    # sql_create_pessoa = '''CREATE TABLE Pessoa (
    #                         cpf INTEGER NOT NULL,
    #                         nome TEXT NOT NULL,
    #                         nascimento DATE NOT NULL,
    #                         oculos BOOLEAN NOT NULL,
    #                         PRIMARY KEY (cpf));'''
    # sql_create_marca = '''CREATE TABLE Marca (
    #                             id INTEGER NOT NULL,
    #                             nome TEXT NOT NULL,
    #                             sigla CHARACTER(2) NOT NULL,
    #                             PRIMARY KEY (id)
    #                             );'''
    #
    # sql_create_veiculo = '''CREATE TABLE Veiculo (
    #                             placa CHARACTER(7) NOT NULL,
    #                             ano INTEGER NOT NULL,
    #                             cor TEXT NOT NULL,
    #                             proprietario INTEGER NOT NULL,
    #                             marca INTEGER NOT NULL,
    #                             PRIMARY KEY (placa),
    #                             FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
    #                             FOREIGN KEY(marca) REFERENCES Marca(id)
    #                             );'''
    # cursor.execute(sql_create_marca)
    # cursor.execute(sql_create_veiculo)
    # conexao.commit()
except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()