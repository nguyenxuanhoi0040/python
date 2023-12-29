import tkinter as tk
from tkinter import font

def change_font(label, font_name):
    selected_font = font.Font(family=font_name, size=12, weight="bold")
    label.config(font=selected_font)

def create_window():
    # Tạo một cửa sổ
    window = tk.Tk()

    # Đặt tiêu đề cho cửa sổ
    window.title("Chương trình GUI Tkinter")

    # Thêm một nhãn vào cửa sổ
    label = tk.Label(window, text="Chào mừng bạn đến với Tkinter!")
    label.pack(padx=20, pady=20)  # Cài đặt kích thước và khoảng cách

    # Tạo một danh sách kiểu phông chữ
    font_names = ["Arial", "Times New Roman", "Courier New"]

    # Tạo một Menu để chọn kiểu phông chữ
    font_menu = tk.Menu(window, tearoff=0)
    for font_name in font_names:
        font_menu.add_command(label=font_name, command=lambda f=font_name: change_font(label, f))

    # Thêm menu kiểu phông chữ vào cửa sổ
    font_menu_label = tk.Label(window, text="Chọn kiểu phông chữ:")
    font_menu_label.pack(pady=5)
    font_menu_button = tk.Menubutton(window, text="Kiểu phông chữ", menu=font_menu)
    font_menu_button.pack(pady=5)

    # Bắt đầu vòng lặp sự kiện
    window.mainloop()

if __name__ == "__main__":
    # Gọi hàm để tạo cửa sổ
    create_window()
