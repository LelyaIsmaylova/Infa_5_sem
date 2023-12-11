def print_coroutine():
    a = "start"
    b = 0
    l = []
    c = 0
    d = 0
    count = 0
  
    while True:
        a = yield a
        if a.isdigit():
            a = int(a)
            b += a
            l.append(a)
            count = len(l)
            c = b / count
            d = b / count - c 
            print("Got value", a)
        else:
            if a == 'mean':
                print('mean', c)
            elif a == 'var':
                print('var', d)
            elif a == 'count':
                print('count', count)


coroutine = print_coroutine()
print(neat(coroutine))

while True:
    n = input()
    print(coroutine.send(n))
