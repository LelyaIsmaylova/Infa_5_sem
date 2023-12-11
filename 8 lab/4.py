from itertools import product

def get_cartesian_product(a, b):
    return list(product(a, b))

result = get_cartesian_product([1, 2], [3, 4])
print(result)
