# Định lớp cơ sở Tam giác
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

# Lớp Tam giác vuông thừa kế từ Tam giác
class RightTriangle(Triangle):# tam giac vuong
    def __init__(self, base, height):
        super().__init__(base, height, (base**2 + height**2)**0.5)

# Lớp Tam giác cân thừa kế từ Tam giác
class IsoscelesTriangle(Triangle): #tam giac can
    def __init__(self, base, legs):
        super().__init__(base, legs, legs)

# Lớp Tam giác đều thừa kế từ Tam giác cân
class EquilateralTriangle(IsoscelesTriangle): #tam giac deu
    def __init__(self, side):
        super().__init__(side, side)

# Nhập thông tin cho một Tam giác
side1 = float(input("Nhập độ dài cạnh 1: "))
side2 = float(input("Nhập độ dài cạnh 2: "))
side3 = float(input("Nhập độ dài cạnh 3: "))

# Tạo một đối tượng Tam giác
triangle = Triangle(side1, side2, side3)

# Kiểm tra xem Tam giác có phải là Tam giác vuông, Tam giác cân hoặc Tam giác đều
if (
    side1 == side2 == side3 and
    side1 > 0 and side2 > 0 and side3 > 0
):
    triangle_type = "Tam giác đều"
elif (
    side1 == side2 or
    side1 == side3 or
    side2 == side3
):
    triangle_type = "Tam giác cân"
else:

    triangle_type = "Tam giác thường"

# In loại Tam giác
print(f"Đây là một {triangle_type}.")
