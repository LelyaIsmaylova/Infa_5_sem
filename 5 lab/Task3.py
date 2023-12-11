class Mother:
    def str(self):
        return "Это материнский класс"

class Daughter(Mother):
    def str(self):
        return "Это дочерний класс"

mother = Mother()
daughter = Daughter()

print(mother)
print(daughter)
