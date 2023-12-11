class Shape:
    def init(self, w, h) -> None:
        self.w = w
        self.h = h

class Triangle(Shape):
    def get_area(self):
        return 0.5 * self.w * self.h

class Rectangle(Shape):
    def get_area(self):
        return self.w * self.h
    
rec = Rectangle(20, 40)
tri = Triangle(20, 40)

print(rec.get_area())
print(tri.get_area())
