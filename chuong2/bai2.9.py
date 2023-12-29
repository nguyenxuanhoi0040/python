import json
json_data = '''
{
  "ten_cong_ty": "Công ty TNHH Đất Việt",
  "dia_chi": "abc Giải Phóng - Hà Nội",
  "don_vi": [
    {"ten_don_vi": "Đơn vị A1", "so_nhan_vien": 20},
    {"ten_don_vi": "Đơn vị A2", "so_nhan_vien": 15},
    {"ten_don_vi": "Đơn vị A3", "so_nhan_vien": 25},
    {"ten_don_vi": "Đơn vị A4", "so_nhan_vien": 30},
    {"ten_don_vi": "Đơn vị A5", "so_nhan_vien": 10}
  ]
}
'''
def thong_ke_nhan_vien(json_data):
    # Đọc dữ liệu từ JSON
    data = json.loads(json_data)

    # In thông tin công ty
    print("Tên công ty:", data["ten_cong_ty"])
    print("Địa chỉ:", data["dia_chi"])
    
    # Tổng số nhân viên
    tong_so_nhan_vien = sum(unit["so_nhan_vien"] for unit in data["don_vi"])
    print("Tổng số nhân viên:", tong_so_nhan_vien)

    # Thống kê nhân viên theo đơn vị
    print("\nThống kê nhân viên theo đơn vị")
    for index, don_vi in enumerate(data["don_vi"], start=1):
        ten_don_vi = don_vi["ten_don_vi"]
        so_nhan_vien = don_vi["so_nhan_vien"]
        ty_le = (so_nhan_vien / tong_so_nhan_vien) * 100

        print(f"{index}./Tên đơn vị: {ten_don_vi}.")
        print(f" - Số nhân viên: {so_nhan_vien}.")
        print(f" - Tỷ lệ: {ty_le:.2f}%.\n")
# Gọi hàm thống kê nhân viên
thong_ke_nhan_vien(json_data)
