with open('task.txt', 'r') as file:
    for line in file.readlines():
        print(line[:-1])
