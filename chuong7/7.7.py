import tkinter as tk

def calculate_sum():
    try:
        n = int(entry.get())
        result = sum(range(1, n + 1))
        result_label.config(text=f"Tổng '1+2+...+{n}' là: {result}")
    except ValueError:
        result_label.config(text="Vui lòng nhập một số nguyên.")

# Tạo cửa sổ
window = tk.Tk()
window.title("Tính tổng 1+2+...+N")

# Tạo nhãn và ô nhập liệu
label = tk.Label(window, text="Nhập số nguyên N:")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Tạo nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Tạo nút và liên kết nó với hàm calculate_sum
calculate_button = tk.Button(window, text="Tính tổng", command=calculate_sum)
calculate_button.pack()

# Chạy vòng lặp chính
window.mainloop()
