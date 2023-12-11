maximum = None

while True:
    num = input("Введите элементы последовательности: ")
    if num == "End":
        break

    try:
        N = float(num)
        if maximum is None or N > maximum:
            maximum = N

    except ValueError:
        print("Последовательность была задана некорректно.")

if maximum is not None:
    print("Максимальное число последовательности:", maximum)
else:
    print("Последовательность была задана некорректно.")