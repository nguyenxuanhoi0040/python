import tkinter as tk
from tkinter import simpledialog

def show_dialog():
    name = simpledialog.askstring("Nhập thông tin", "Nhập tên của bạn:")
    age = simpledialog.askinteger("Nhập thông tin", "Nhập tuổi của bạn:")

    if age is not None:
        if age >= 18:
            message = f"Xin chào {name}! Bạn đã trưởng thành, {age} tuổi."
        else:
            message = f"Bạn còn nhỏ tuổi, {name}! Tuổi của bạn là {age}."

        # Hiển thị thông báo
        tk.messagebox.showinfo("Thông báo", message)

# Tạo cửa sổ chính
root = tk.Tk()
root.withdraw()  # Ẩn cửa sổ chính

# Gọi hộp thoại nhập thông tin
show_dialog()

# Main loop
root.mainloop()
