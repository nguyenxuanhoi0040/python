import sqlite3
def xoa_hang(database_path,table_name,column_key,key_value):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    sql = f"DELETE FROM {table_name} WHERE {column_key} = ?"
    cursor.execute(sql,(key_value,))
    conn.commit()
    conn.close()

database_path = 'my_database2.db'
table_name = 'example_table'
column_key = 'name'
key_value = 'id'
xoa_hang(database_path,table_name,column_key,key_value)