def swap(func):
    def wrapper(*a, **b):
        reverse_a = a[::-1]
        return func(*reverse_a, **b)
    return wrapper

@swap
def example(*a):
    return a
