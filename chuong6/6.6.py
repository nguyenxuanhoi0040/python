import threading

class EvenOddPrinter:
    def __init__(self, limit):
        self.limit = limit
        self.current_number = 0
        self.lock = threading.Lock()

    def print_even(self):
        while self.current_number <= self.limit:
            with self.lock:
                if self.current_number % 2 == 0:
                    print(f"Chẵn: {self.current_number}")
                    self.current_number += 1

    def print_odd(self):
        while self.current_number <= self.limit:
            with self.lock:
                if self.current_number % 2 != 0:
                    print(f"Lẻ: {self.current_number}")
                    self.current_number += 1

if __name__ == "__main__":
    # Đặt ngưỡng giới hạn
    threshold = 20

    # Tạo một đối tượng EvenOddPrinter với ngưỡng nhất định
    printer = EvenOddPrinter(threshold)

    # Tạo hai luồng, mỗi luồng thực hiện một phương thức của đối tượng EvenOddPrinter
    even_thread = threading.Thread(target=printer.print_even)
    odd_thread = threading.Thread(target=printer.print_odd)

    # Bắt đầu thực thi cả hai luồng
    even_thread.start()
    odd_thread.start()

    # Chờ cho cả hai luồng hoàn thành
    even_thread.join()
    odd_thread.join()

    print("Done")
