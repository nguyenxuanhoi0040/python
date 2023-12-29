from datetime import date

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

class Employee:
    def __init__(self, ho_ten, ngay_sinh, ngay_vao_cong_ty):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.ngay_vao_cong_ty = ngay_vao_cong_ty

    def tinh_so_nam_lam_viec(self):
        today = date.today()
        return today.year - self.ngay_vao_cong_ty.year

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Ngày sinh: {self.ngay_sinh.day}/{self.ngay_sinh.month}/{self.ngay_sinh.year}")
        print(f"Ngày vào công ty: {self.ngay_vao_cong_ty.day}/{self.ngay_vao_cong_ty.month}/{self.ngay_vao_cong_ty.year}")
        print(f"Số năm làm việc: {self.tinh_so_nam_lam_viec()} năm")

# Hàm nhập thông tin nhân viên từ bàn phím
def nhap_danh_sach_nhan_vien():
    danh_sach_nhan_vien = []
    so_nhan_vien = int(input("Nhập số lượng nhân viên: "))
    
    for i in range(so_nhan_vien):
        ho_ten = input("Nhập họ tên nhân viên: ")

        ngay_sinh = Date(int(input("Nhập ngày sinh (ngày): "))/ int(input("Nhập ngày sinh (tháng): "))/int(input("Nhập ngày sinh (năm): ")))

        ngay_vao_cong_ty = Date(int(input("Nhập ngày vào công ty (ngày): "))/int(input("Nhập ngày vào công ty (tháng): "))/int(input("Nhập ngày vào công ty (năm): ")))

        nhan_vien = Employee(ho_ten, ngay_sinh, ngay_vao_cong_ty)
        danh_sach_nhan_vien.append(nhan_vien)

    return danh_sach_nhan_vien

# Hàm in danh sách nhân viên
def in_danh_sach_nhan_vien(danh_sach_nhan_vien):
    print("\nDanh sách nhân viên:")
    for nhan_vien in danh_sach_nhan_vien:
        nhan_vien.in_thong_tin()

# Chương trình chính
danh_sach_nhan_vien = nhap_danh_sach_nhan_vien()
in_danh_sach_nhan_vien(danh_sach_nhan_vien)
