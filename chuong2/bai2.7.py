import json

# Tạo một đối tượng Python (dictionary) để chuyển đổi thành JSON
my_dict = {
    "name": "Hoi",
    "age": 19,
    "city": "Hung Yen"
}

# Chuyển đối tượng thành chuỗi JSON với việc thêm khoảng trắng (indent=2) để làm cho chuỗi dễ đọc hơn
chuoi_json = json.dumps(my_dict, indent=2)

# In ra chuỗi JSON
print(chuoi_json)
