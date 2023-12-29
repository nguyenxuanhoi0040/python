import tkinter as tk

def create_window():
    # Tạo một cửa sổ
    window = tk.Tk()

    # Đặt tiêu đề cho cửa sổ
    window.title("Chương trình GUI Tkinter")

    # Bắt đầu vòng lặp sự kiện
    window.mainloop()

if __name__ == "__main__":
    # Gọi hàm để tạo cửa sổ
    create_window()
