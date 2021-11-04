import sqlite3 as connector

try:
    conexao = connector.connect("dev-python-manha.sqlite")
    cursor = conexao.cursor()

    sqr_query = '''CREATE TABLE Pessoa (
                        cpf INTEGER NOT NULL,
                        nome TEXT NOT NULL,
                        nascimento DATE NOT NULL,
                        oculos BOOLEAN NOT NULL,
                        PRIMARY KEY (cpf));'''

    cursor.execute(sqr_query)
    conexao.commit()

except connector.DatabaseError as err:
    print("Erro de Banco de Dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()
