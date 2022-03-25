from contextlib import contextmanager

import pymysql.cursors


@contextmanager
def databaseConnection():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conn
    finally:
        conn.close()


# with databaseConnection() as connection, connection.cursor() as cursor:
#     query = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#     cursor.execute(query, ('Jack', 'Monroe', 16, 90))
#     connection.commit()

# with databaseConnection() as connection, connection.cursor() as cursor:
#     query = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#
#     data = [
#         ('John', 'Marston', 26, 61),
#         ('Devin', 'Lee', 12, 54),
#         ('Catherine', 'Banks', 22, 49)
#     ]
#     cursor.executemany(query, data)
#     connection.commit()

# with databaseConnection() as connection, connection.cursor() as cursor:
#     query = 'UPDATE clientes SET nome=%s WHERE id=%s'
#     cursor.execute(query, ('Francine', 7,))
#     connection.commit()


# with databaseConnection() as connection, connection.cursor() as cursor:
#     query = 'DELETE FROM clientes WHERE id = %s'
#     cursor.execute(query, (8,))
#     connection.commit()

# with databaseConnection() as connection, connection.cursor() as cursor:
#     query = 'DELETE FROM clientes WHERE id IN (%s, %s, %s, %s, %s)'
#     cursor.execute(query, (1, 2, 3, 4, 5))

# # # same as:
#     query = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#     cursor.execute(query, (1, 5))
#     connection.commit()


with databaseConnection() as connection, connection.cursor() as cursor:
    cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
    results = cursor.fetchall()

    for row in results:
        print(row)
