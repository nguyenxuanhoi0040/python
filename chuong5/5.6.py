import sqlite3

def count_records(database_path, table_name):
    try:
        # Kết nối đến cơ sở dữ liệu
        conn = sqlite3.connect(database_path)
        
        # Tạo một đối tượng cursor để thực thi các truy vấn SQL
        cursor = conn.cursor()

        # Thực hiện truy vấn để đếm số bản ghi
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")

        # Lấy kết quả của truy vấn
        record_count = cursor.fetchone()[0]

        # Đóng kết nối đến cơ sở dữ liệu
        conn.close()

        return record_count

    except sqlite3.Error as e:
        print("Error:", e)
        return None

# Thay đổi đường dẫn đến tệp cơ sở dữ liệu và tên bảng của bạn
database_path = "my_database2.db"
table_name = "example_table"

# Lấy và in số bản ghi
record_count = count_records(database_path, table_name)
if record_count is not None:
    print(f"Số bản ghi trong bảng '{table_name}': {record_count}")
