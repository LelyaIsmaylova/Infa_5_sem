from itertools import permutations
def get_permutations(s, n):
    result = [''.join(p) for p in permutations(s, n)]
    result.sort()
    print(result)

get_permutations("doctor", 2)
