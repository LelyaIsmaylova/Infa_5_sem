def maximize(lists, m):
    max_result = 0
    for combo in product(*lists):
        result = sum(x**2 for x in combo) % m
        max_result = max(max_result, result)
    print(max_result)
  
lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]

maximize(lists, m=1000)
