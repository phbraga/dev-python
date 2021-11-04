import sqlite3 as conector
from pessoa import Pessoa

try:
    conexao = conector.connect("dev-python-manha.sqlite")
    cursor = conexao.cursor()

    nome = input("Informe o seu nome: ")
    cpf = int(input("Informe o seu CPF: "))
    nascimento = input("Informe sua data de nascimento: ")
    oculos = int(input("Você usa óculos (1- Sim, 2- Nao): "))
    pessoa = Pessoa(cpf, nascimento, nome, oculos)

    # sqr_query = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?);'''
    # cursor.execute(sqr_query, (cpf, nome, nascimento, oculos))

    sqr_query = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (:cpf, :nome, :nascimento, :oculos);'''
    # cursor.execute(sqr_query, {"cpf": cpf,
    #                            "nome": nome,
    #                            "nascimento": nascimento,
    #                            "oculos": oculos})
    cursor.execute(sqr_query, vars(pessoa))

    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()