from itertools import combinations, combinations_with_replacement

def get_combinations_with_r(s, n):
    result = list(combinations_with_replacement(s, n))
    result = [''.join(item) for item in result]
    print(result)

get_combinations_with_r("doctor", 2)
