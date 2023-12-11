list = []
for i in range(1, 50):
    n = i*i
    if n < 2500 and n % 10 == 1:
        list.append(n)

print(list)