x = "wrong number"
try:
    number = int(x)
except ValueError as e:
    print("Произошла ошибка ValueError:", str(e))

Произошла ошибка ValueError: invalid literal for int() with base 10: 'wrong number'
