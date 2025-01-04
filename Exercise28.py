# Nhập chuỗi số
input_string = "5;7;8;-2;8;11;13;9;10"

# Tách chuỗi bằng dấu ";" và chuyển mỗi phần tử thành số nguyên
numbers = [int(num) for num in input_string.split(";")]

# Xuất các chữ số trên các dòng riêng biệt
print("Numbers in the string:")
for num in numbers:
    print(num)

# Thống kê số chẵn
even_numbers = [num for num in numbers if num % 2 == 0]
print("\nEven Numbers:")
print(even_numbers)

# Thống kê số âm
negative_numbers = [num for num in numbers if num < 0]
print("\nNegative Numbers:")
print(negative_numbers)

# Thống kê số nguyên tố
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in numbers if is_prime(num)]
print("\nPrime Numbers:")
print(prime_numbers)

# Tính giá trị trung bình
average_value = sum(numbers) / len(numbers)
print("\nAverage Value:")
print(average_value)
