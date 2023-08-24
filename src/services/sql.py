import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Создание таблицы, если она еще не создана
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        university TEXT,
        course TEXT,
        service TEXT
    )
''')
conn.commit()

