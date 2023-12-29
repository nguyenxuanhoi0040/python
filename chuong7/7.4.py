import tkinter as tk

def submit():
    name = name_entry.get()
    student_id = id_entry.get()
    password = password_entry.get()
    
    # You can perform further actions with the entered information here
    
    # For now, let's just print the information
    print("Name:", name)
    print("Student ID:", student_id)
    print("Password:", password)

# Tạo cửa sổ
window = tk.Tk()
window.title("Student Information Form")

# Tạo ba hộp văn bản và nhãn tương ứng
name_label = tk.Label(window, text="Name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

id_label = tk.Label(window, text="Student ID:")
id_label.pack()

id_entry = tk.Entry(window)
id_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()

password_entry = tk.Entry(window, show="*")  # show="*" để ẩn mật khẩu
password_entry.pack()

# Tạo nút Gửi
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

# Chạy vòng lặp chính
window.mainloop()
