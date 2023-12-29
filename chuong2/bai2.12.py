import requests
#Đọc dữ liệu từ API 
response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
#số lượng bài post
post_id = 1
so_luong_bai_post = 3
#Kiểm tra xem yêu cầu thành công hay không?
if response.status_code == 200:
    #Nếu thành công,lấy dữ liệu từ
    sach_data = response.json()
    #Giới hạn bài post
    sach_data = sach_data[:so_luong_bai_post]
    print(f"Danh sách các bài post nổi bật với post_ID = {post_id}:\n")
    
    for post in sach_data:
        print("PostId:",post["id"])
        print("ID:",post["id"])
        print("Name:",post["name"])
        print("Email:",post["email"])
        print("Body:",post["body"])
        print("==================================")
else:
    print("yêu cầu không thành công.")