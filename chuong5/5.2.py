import sqlite3

# Tạo kết nối đến cơ sở dữ liệu SQLite trong bộ nhớ
conn = sqlite3.connect(':memory:')

# Lấy đối tượng cursor để thực hiện các truy vấn SQL
cursor = conn.cursor()

# Thực hiện các thao tác trên cơ sở dữ liệu trong bộ nhớ
# Ví dụ: Tạo một bảng đơn giản
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Thêm dữ liệu vào bảng
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('A', 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('b', 30))


# In ra dữ liệu từ bảng
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Đóng kết nối đến cơ sở dữ liệu trong bộ nhớ
conn.close()
