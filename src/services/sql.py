import sqlite3


# Создаем базу данных
def create_database():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            lastname TEXT,
            age INTEGER,
            university TEXT, 
            faculty TEXT
        )
    ''')

    conn.commit()
    conn.close()


create_database()


