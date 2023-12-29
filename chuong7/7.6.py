import tkinter as tk

def reverse_word():
    input_word = entry.get()
    reversed_word = input_word[::-1]
    result_label.config(text="Từ ngược lại là: " + reversed_word)

# Tạo cửa sổ
window = tk.Tk()
window.title("Reverse Word App")

# Tạo nhãn và ô nhập liệu
label = tk.Label(window, text="Nhập từ:")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Tạo nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Tạo nút và liên kết nó với hàm reverse_word
reverse_button = tk.Button(window, text="Đảo ngược", command=reverse_word)
reverse_button.pack()

# Chạy vòng lặp chính
window.mainloop()
