from itertools import combinations, combinations_with_replacement

def get_combinations(s, n):
    result = []
    for k in range(1, n + 1):
        for combo in combinations(s, k):
            result.append(''.join(combo))
    print(result)

get_combinations("doctor", 2)
