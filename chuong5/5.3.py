import sqlite3

# Kết nối đến cơ sở dữ liệu (nếu không tồn tại, nó sẽ được tạo mới)
conn = sqlite3.connect('my_database1.db')

# Tạo đối tượng cursor để thực hiện các truy vấn SQL
cursor = conn.cursor()

# Tạo bảng với các trường mong muốn (ví dụ: id, name, age)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Lưu thay đổi và đóng kết nối
conn.commit()
