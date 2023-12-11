minimum = None

while True:
    num = input("Введите элементы последовательности: ")
    if num == "End":
        break

    try:
        N = float(num)
        if minimum is None or N < minimum:
            minimum = N

    except ValueError:
        print("Последовательность была задана некорректно.")

if minimum is not None:
    print("Минимальное число последовательности:", minimum)
else:
    print("Последовательность была задана некорректно.")