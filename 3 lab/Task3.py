import os

def find_directories(root_dir):
    py_dir = set()
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                py_dir.add(root)
    return sorted(py_dir)

root_dir = '.'
py_dir = find_directories(root_dir)

with open('Task3.txt', 'w') as result_file:
    for dir in py_dir:
        result_file.write(dir + '\n')
