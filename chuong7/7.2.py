import tkinter as tk

def create_window():
    # Tạo một cửa sổ
    window = tk.Tk()

    # Đặt tiêu đề cho cửa sổ
    window.title("Chương trình GUI Tkinter")

    # Thêm một nhãn vào cửa sổ
    label = tk.Label(window, text="Chào mừng bạn đến với Tkinter!")
    label.pack(padx=20, pady=20)  # Cài đặt kích thước và khoảng cách

    # Bắt đầu vòng lặp sự kiện
    window.mainloop()

if __name__ == "__main__":
    # Gọi hàm để tạo cửa sổ
    create_window()
