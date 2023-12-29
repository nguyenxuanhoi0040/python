import sqlite3
#Tạo hoặc kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('my_database.db')
# Lấy đối tượng cursor để thực hiện các truy vấn SQL
cursor = conn.cursor()
# In ra phiên bản của SQLite
cursor.execute("SELECT SQLITE_VERSION()")
version = cursor.fetchone()
print(f"SQLite version: {version[0]}")
# Đóng kết nối đến cơ sở dữ liệu
conn.close()
