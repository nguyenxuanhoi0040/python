import tkinter as tk

def list_factors():
    try:
        n = int(entry.get())
        factors = [i for i in range(1, n + 1) if n % i == 0]
        result_label.config(text=f"Ước của {n}: {factors}")
    except ValueError:
        result_label.config(text="Vui lòng nhập một số nguyên.")

# Tạo cửa sổ
window = tk.Tk()
window.title("Liệt kê ước của một số nguyên")

# Tạo nhãn và ô nhập liệu
label = tk.Label(window, text="Nhập số nguyên N:")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Tạo nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()


# Tạo nút và liên kết nó với hàm list_factors
list_factors_button = tk.Button(window, text="Liệt kê ước", command=list_factors)
list_factors_button.pack()


# Chạy vòng lặp chính
window.mainloop()
