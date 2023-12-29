import threading
import requests

def make_http_request(url):
    response = requests.get(url)
    print(f"URL: {url}, Status Code: {response.status_code}")

if __name__ == "__main__":
    # Đưa danh sách các URL bạn muốn thực hiện yêu cầu HTTP vào đây
    urls = ["https://www.example.com", "https://www.example.org", "https://www.example.net"]

    # Tạo một luồng cho mỗi yêu cầu HTTP
    threads = []
    for url in urls:
        thread = threading.Thread(target=make_http_request, args=(url,))
        threads.append(thread)
        thread.start()

    # Chờ cho tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

    print("All requests completed.")
