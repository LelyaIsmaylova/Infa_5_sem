class Animal:
    def init(self, name, age):
        self._name = name
        self._age = age

    def description(self):
        return f"Name: {self._name}, Age: {self._age}"


class Zebra(Animal):
    def description(self):
        return f"Name: {self._name}, Age: {self._age}, Species: Zebra"


class Dolphin(Animal):
    def description(self):
        return f"Name: {self._name}, Age: {self._age}, Species: Dolphin"


zebra = Zebra("Stripes", 5)
dolphin = Dolphin("Dolly", 7)

print(zebra.description())
print(dolphin.description())
