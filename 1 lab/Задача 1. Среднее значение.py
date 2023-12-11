sum = 0
amount = 0

while True:
    num = input("Введите элементы последовательности: ")
    if num == "End":
        break
    sum += float(num)
    amount += 1

if amount > 0:
    average = sum / amount
    print("Среднее значение последовательности: ", average)
else:
    print("Последовательность была задана некорректно.")