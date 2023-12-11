import sys

def fibonacci(n):
    fibonacci_sequence = [0, 1]
    if n <= 0:
        return []
    while len(fibonacci_sequence) < n:
        next_member = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fib_sequence.append(next_member)
    return fibonacci_sequence[-1]

print(fibonacci(int(sys.argv[-1])))
