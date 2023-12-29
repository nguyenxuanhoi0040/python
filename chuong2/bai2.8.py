import json

# Tạo một đối tượng từ điển Python (đã sắp xếp theo khóa)
my_dict = {
    "name": "Hoi",
    "age": 19,
    "city": "Hung Yen"
}

# Chuyển đối tượng từ điển thành chuỗi JSON với việc sắp xếp theo khóa và thụt lề là 4
chuoi_json = json.dumps(my_dict, indent=4,sort_keys=True)

# In ra chuỗi JSON
print(chuoi_json)
