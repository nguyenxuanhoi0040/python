import sqlite3

def create_table_and_insert_data(database_path):
    try:
        # Kết nối đến cơ sở dữ liệu hoặc tạo nếu chưa tồn tại
        connection = sqlite3.connect(database_path)
        
        # Tạo một đối tượng cursor để thực thi các truy vấn SQL
        cursor = connection.cursor()

        # Tạo bảng
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS example_table (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            );
        ''')

        # Chèn một số bản ghi vào bảng
        cursor.execute("INSERT INTO example_table (name, age) VALUES (?, ?);", ("Nguyễn Văn A", 5))
        cursor.execute("INSERT INTO example_table (name, age) VALUES (?, ?);", ("Ngô Thị B", 25))
        cursor.execute("INSERT INTO example_table (name, age) VALUES (?, ?);", ("Trần Thị C", 18))
        cursor.execute("INSERT INTO example_table (name, age) VALUES (?, ?);", ("Nguyễn Văn D", 40))

        # Lưu thay đổi và đóng kết nối đến cơ sở dữ liệu
        connection.commit()
        connection.close()

        print("Đã tạo thành công !")

    except sqlite3.Error as e:
        print("Error:", e)

# Thay đổi đường dẫn đến tệp cơ sở dữ liệu của bạn
database_path = "my_database2.db"
create_table_and_insert_data(database_path)
