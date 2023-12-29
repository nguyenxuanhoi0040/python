import threading

def print_thread_name():
    thread_name = threading.current_thread().name
    print(f"Tên luồng: {thread_name}")

# Tạo 5 luồng
threads = []
for i in range(5):
    thread = threading.Thread(target=print_thread_name, name=f"Thread-{i}")
    threads.append(thread)

# Bắt đầu tất cả các luồng
for thread in threads:
    thread.start()

# Kết thúc luồng
for thread in threads:
    thread.join()
print('Done!')
