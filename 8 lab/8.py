from itertools import groupby

def compress_string(s):
    compressed = [(len(list(group)), int(key)) for key, group in groupby(s)]
    print(compressed)

compress_string('12345')
