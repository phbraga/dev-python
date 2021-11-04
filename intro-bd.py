import sqlite3 as connector

try:
    conexao = connector.connect("dev-python-manha.sqlite")
    cursor = conexao.cursor()

    sqr_query = '''SELECT nome, matricula FROM Aluno;'''
    cursor.execute(sqr_query)

    alunos = cursor.fetchall()

    for nome, matricula in alunos:
        print(f"Nome: {nome}, Matricula: {matricula}")

except connector.DatabaseError as err:
    print("Erro de Banco de Dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()
