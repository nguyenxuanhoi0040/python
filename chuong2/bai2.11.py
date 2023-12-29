import requests
#Đọc dữ liệu từ API 
response = requests.get('https://jsonplaceholder.typicode.com/posts')
#Kiểm tra xem yêu cầu thành công hay không?
if response.status_code == 200:
    #Nếu thành công,lấy dữ liệu từ
    json_data = response.json()

    print(f'Tổng số bài post:{len(json_data)}\n')

    for post in json_data:
        print("userID:",post["id"])
        print("ID:",post["id"])
        print("Tiêu đề:",post["title"])
        print("Nội Dung:",post["body"])
        print("==================================")
else:
    print("yêu cầu không thành công.")