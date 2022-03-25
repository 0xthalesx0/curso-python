import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')


# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#                {'nome': 'Joãozinho', 'peso': 25})
#
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#                {'id': None, 'nome': 'Daniel', 'peso': 113})
# conexao.commit()

# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
#                {'nome': 'Joana', 'id': 2})
#
# cursor.execute('UPDATE clientes SET nome=?, peso=? WHERE id=?',
#                ('Jeremy', 150, 3))
# conexao.commit()

# cursor.execute(f'DELETE FROM clientes WHERE id=:id', {'id': 2})
# conexao.commit()

# cursor.execute('SELECT * FROM clientes')


for linha in cursor.fetchall():
    numeroID, nome, peso = linha
    # print(f'O id {numeroID} pertence à {nome} e tem {peso} quilos')
    print(numeroID, nome, peso)
cursor.close()
conexao.close()
