import json

from datetime import datetime

def ghi_giao_dich_cho_tap_tin(giao_dich):
    # Lấy thông tin ngày hiện tại
    ngay_hien_tai = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    # Tạo tên tập tin dựa trên ngày hiện tại
    ten_tap_tin = f"{ngay_hien_tai}.json"

    # Lưu danh sách các giao dịch vào tập tin JSON
    with open(ten_tap_tin, 'w', encoding='utf-8') as file:
        json.dump(giao_dich, file, ensure_ascii=False, indent=2)

# Hàm quản lý giao dịch
def quan_ly_giao_dich():
    giao_dich = []
#Tạo 1 vòng lặp để hỏi người dùng có muốn giao dịch nữa không
    while True:
        tiep_tuc = input("Bạn muốn tiếp tục thực hiện giao dịch không? (c/k): ")
        #Nếu không có giao dịch nào sẽ 0 có giá trị nào trong tập tin
        if tiep_tuc.lower() != 'c':
            break
        # Giao dịch được thêm vào danh sách
        giao_dich.append({"loai": "Tien", "so_tien": 10})

    ghi = input("Bạn muốn ghi vào tập tin không? (1: Có, 0: Không): ")

    if ghi == '1':
        ghi_giao_dich_cho_tap_tin(giao_dich)
        print("Đã ghi vào tập tin.")
    else:
        print("Không ghi vào tập tin.")


# Thực hiện quản lý giao dịch
quan_ly_giao_dich()
