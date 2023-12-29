import threading

def print_even_numbers():
    for i in range(30, 51, 2):
        print(f"Chẵn: {i}")

def print_odd_numbers():
    for i in range(31, 51, 2):
        print(f"Lẻ: {i}")

if __name__ == "__main__":
    # Tạo hai luồng
    even_thread = threading.Thread(target=print_even_numbers)
    odd_thread = threading.Thread(target=print_odd_numbers)

    # Bắt đầu thực thi hai luồng
    even_thread.start()
    odd_thread.start()

    # Chờ cho cả hai luồng hoàn thành
    even_thread.join()
    odd_thread.join()

    print("Done")
