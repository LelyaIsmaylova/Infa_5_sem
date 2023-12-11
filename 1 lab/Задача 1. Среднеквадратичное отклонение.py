import math
numbers = []

while True:
    value = input("Введите элементы последовательности: ")
    if value == "End":
        break
    else:
        try:
            number = float(value)
            numbers.append(number)
        except ValueError:
            print("Последовательность была задана некорректно.")

if len(numbers) > 0:
    mean = sum(numbers) / len(numbers)
    squared_diffs = [(number - mean) ** 2 for number in numbers]
    variance = sum(squared_diffs) / len(numbers)
    std_deviation = math.sqrt(variance)
    print(f"Среднеквадратичное отклонение: {std_deviation:.2f}")
else:
    print("Последовательность была задана некорректно.")