#Да, возможно
class Node:
    def init(self, value, nxt=None):
        self.value = value
        self.nxt = nxt

    def get_value(self):
        return self.value

    def get_next(self):
        return self.nxt


class LinkedList:
    def init(self):
        self.start = None
        self.length = 0
        self.last = None

    def add(self, value):
        elem = Node(value)
        if self.start is None:
            self.start = elem
            self.last = elem
        else:
            self.last.nxt = elem
            self.last = elem
        self.length += 1

    def len(self):
        return self.length

    def getitem(self, idx):
        if idx >= self.length:
            raise IndexError("Index out of range")
        current = self.start
        for i in range(idx):
            current = current.get_next()
        return current.get_value()

    def iter(self):
        self.curr = self.start
        return self

    def __next(self):
        if self.__curr is None:
            raise StopIteration()
        val = self.__curr.get_value()
        self.__curr = self.__curr.get_next()
        return val


lst = LinkedList()
for i in range(10):
    lst.add(i * i)

for item in lst:
    print(item)
