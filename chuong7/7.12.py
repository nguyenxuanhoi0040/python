import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Tính chỉ số BMI
        bmi = weight / (height ** 2)

        # Hiển thị kết quả trong ô BMI
        bmi_result.set(f"Chỉ số BMI: {bmi:.2f}")

        # Kết luận theo chỉ số BMI
        if bmi < 18.5:
            conclusion = "Gầy"
        elif 18.5 <= bmi < 24.9:
            conclusion = "Bình thường"
        elif 25 <= bmi < 29.9:
            conclusion = "Hơi béo"
        else:
            conclusion = "Béo phì"

        # Hiển thị thông báo kết luận
        messagebox.showinfo("Kết quả", f"Chỉ số BMI của bạn là {bmi:.2f}\nKết luận: {conclusion}")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập cân nặng và chiều cao hợp lệ.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tính chỉ số BMI")

# Tạo và định vị các thành phần trong giao diện
weight_label = tk.Label(root, text="Nhập cân nặng (kg):")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack(pady=10)

height_label = tk.Label(root, text="Nhập chiều cao (m):")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack(pady=10)

calculate_button = tk.Button(root, text="Tính BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

bmi_result = tk.StringVar()
result_label = tk.Label(root, textvariable=bmi_result)
result_label.pack()

# Main loop
root.mainloop()
