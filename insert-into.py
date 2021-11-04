import sqlite3 as connector

try:
    conexao = connector.connect("dev-python-manha.sqlite")
    cursor = conexao.cursor()

    sqr_query = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                    VALUES (12345678900, 'João', '2000-01-31', 1);'''

    cursor.execute(sqr_query)
    conexao.commit()

except connector.DatabaseError as err:
    print("Erro de Banco de Dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()
