#Tạo lớp biểu diễn hình chữ nhật, chu vi , diện tích
class hcn:
    def __init__(self):
        self.c_dai = 0
        self.c_rong = 0
    
    def dl_canh_hcn(self):
        self.c_dai = float(input("Nhập chiều dài:"))
        self.c_rong = float(input("Nhập chiều rộng:"))

    def chuvi(self):
        chu_vi = (self.c_dai + self.c_rong) * 2
        return chu_vi
    
    def dientich(self):
        dien_tich = self.c_dai * self.c_rong
        return dien_tich
    
    def thongso(self):
        print("Thông số hình chữ nhật:")
        print(f'Chiều dài: {self.c_dai}')
        print(f'Chiều rộng: {self.c_rong}')
        print(f'Chu vi:{self.chuvi()}')
        print(f'Diện tích: {self.dientich()}')

Hinh_chu_nhat = hcn()
Hinh_chu_nhat.dl_canh_hcn()
Hinh_chu_nhat.thongso()