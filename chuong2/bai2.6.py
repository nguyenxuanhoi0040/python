import json

# Chuỗi JSON mẫu
json_str = '{"name": "Hoi", "age": 19, "city": "Hung Yen"}'

# Chuyển đổi chuỗi JSON thành đối tượng Python (dictionary)
py_obj = json.loads(json_str)

# In ra đối tượng Python
print(py_obj)

# Truy cập các giá trị trong đối tượng Python
name = py_obj["name"]
age = py_obj["age"]
city = py_obj["city"]

# In ra các giá trị
print("Name:", name)
print("Age:", age)
print("City:", city)