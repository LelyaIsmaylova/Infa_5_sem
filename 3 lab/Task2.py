def write_array(array, file_name):
    with open(file_name, 'w') as file:
        file.writelines(array)

write_array(['TARDIS\n', 'Doctor\n', 'Donna\n'], 'Task2.txt')
