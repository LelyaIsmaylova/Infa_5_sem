import pickle

# сериализация итератора (список)
iterator_data = iter([1, 2, 3, 4, 5])

with open('iterator.pickle', 'wb') as f:
    pickle.dump(iterator_data, f)

with open('iterator.pickle', 'rb') as f:
    deserialized_iterator = pickle.load(f)

# Пример
for item in deserialized_iterator:
    print(item)


# определение класса
class MyClass:
    def __init__(self, value):
        self.value = value

# создание объекта и его сериализации
obj = MyClass(42)

with open('custom_class.pickle', 'wb') as f:
    pickle.dump(obj, f)

# десериализация объекта
with open('custom_class.pickle', 'rb') as f:
    deserialized_obj = pickle.load(f)

# использование
print(deserialized_obj.value)

from collections import deque

# сериализация объекта
deque_data = deque([1, 2, 3, 4, 5])

with open('deque.pickle', 'wb') as f:
    pickle.dump(deque_data, f)

# десериализации объекта
with open('deque.pickle', 'rb') as f:
    deserialized_deque = pickle.load(f)

# использование
print(deserialized_deque)
