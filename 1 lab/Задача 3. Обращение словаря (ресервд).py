elem = {'1': '2', '3': '4', '5': '6'}
mele = dict(reversed(item) for item in elem.items())
print(mele)