import sqlite3

def list_tables(data_path):
    conn = sqlite3.connect(data_path)

    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")

    tables = cursor.fetchall()
    conn.close

    for table in tables:
        print(table[0])

data_path = "my_database.db"
list_tables(data_path)