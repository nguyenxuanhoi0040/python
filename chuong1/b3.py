class PS:
    def __init__(self,tuso,mauso):
        self.tuso = tuso
        self.mauso = mauso
    #Kiểm tra tính hợp lệ của phân số
    def kiem_tra_hop_le(self):
        return self.mauso != 0
    
    def nhap_ps(self):
        tuso = float(input("Nhập tử số:"))
        mauso = float(input("Nhập mẫu số"))
        if mauso == 0:
            print("Mẫu số phải khác 0. Vui lòng nhập lại từ đầu.")
            return
        self.tuso = tuso
        self.mauso = mauso

    def in_ps(self):
        if self.kiem_tra_hop_le():
            print(f'{self.tuso}/{self.mauso}')
        else:
            print("Phân số không hợp lệ!")
    
# Chương trình chính
if __name__ == "__main__":
    phan_so = PS(0, 1)  # Khởi tạo một phân số mặc định

    print("Quản lý phân số.")
    print("1.Nhập phân số")
    print("2.In phân số")
    print("0.Thoát")

    while True:
        lua_chon = int(input("Nhập lựa chọn: "))
        
        if lua_chon == 1:
            phan_so.nhap_ps()
        elif lua_chon == 2:
            phan_so.in_ps()
        elif lua_chon == 0:
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")