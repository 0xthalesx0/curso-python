import sqlite3


def initConnection(archive):
    conn = sqlite3.connect(archive)
    return conn, conn.cursor()


def executeQuery(command):
    def wrapper(*args):
        query, values = command(*args)
        cursor.execute(query, values)
        connection.commit()
    return wrapper


class PhonebookDB:
    def __init__(self):
        pass

    @executeQuery
    def insert(self, name, phone):
        return 'INSERT OR IGNORE INTO phonebook (name, phone) VALUES (?, ?)', (name, phone)

    @executeQuery
    def edit(self, name, phone, id):
        return 'UPDATE OR IGNORE phonebook SET name=?, phone=? WHERE id=?', (name, phone, id)

    @executeQuery
    def delete(self, id):
        return 'DELETE FROM phonebook WHERE id=?', (id,)

    def list(self):
        cursor.execute('SELECT * FROM phonebook')
        self.print_rows()
        pass

    def search(self, value):
        query = 'SELECT * FROM phonebook WHERE name LIKE ?'

        cursor.execute(query, (f'%{value}%',))
        self.print_rows()
        pass

    @staticmethod
    def print_rows():
        for row in cursor.fetchall():
            print(row)


if __name__ == '__main__':
    connection, cursor = initConnection('phonebook.db')
    phonebook = PhonebookDB()
    # phonebook.insert('Luiz', '56756111')
    # phonebook.insert('Maria', '22345678')
    # phonebook.insert('Maria', '22345678')
    # phonebook.insert('Mariano', '22345676')
    # phonebook.insert('Maria Luiza', '22345655')
    # phonebook.insert('Mariana', '22343212')
    # phonebook.insert('João', '32345678')
    # phonebook.insert('Guilherme', '42345678')
    # phonebook.edit('Francis', '13131313', 9)
    # phonebook.delete(10)
    phonebook.list()
    # phonebook.search('Maria')

    cursor.close()
    connection.close()
