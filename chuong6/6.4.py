import threading
def calculate_factorial(start, end, result_dict):
    result = 1
    for i in range(start, end + 1):
        result *= i
    result_dict[start] = result

def parallel_factorial(n, num_threads=4):
    thread_list = []
    result_dict = {}

    # Chia nhỏ dãy số thành các phần cho từng luồng
    chunk_size = n // num_threads
    for i in range(0, n, chunk_size):
        start = i + 1
        end = min(i + chunk_size, n)
        thread = threading.Thread(target=calculate_factorial, args=(start, end, result_dict))
        thread_list.append(thread)
        thread.start()

    # Chờ cho tất cả các luồng hoàn thành
    for thread in thread_list:
        thread.join()

    # Tính tổng tích của từng phần để có kết quả cuối cùng
    final_result = 1
    for key in sorted(result_dict.keys()):
        final_result *= result_dict[key]

    return final_result

if __name__ == "__main__":
    number_to_calculate = 6
    result = parallel_factorial(number_to_calculate)
    print(f"The factorial of {number_to_calculate} is: {result}")
