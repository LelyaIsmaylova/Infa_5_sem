elem = {'1': '2', '3': '4', '5': '6'}
mele = dict((value, key) for key, value in elem.items())
print(mele)