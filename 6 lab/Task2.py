class Vector:

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, factor):
        if isinstance(factor, Vector):
            return self.x * factor.x + self.y * factor.y + self.z * factor.z
        return Vector(factor * self.x, factor * self.y, factor * self.z)

    def __matmul__(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

points_list = [
    Vector(1.2, 2.4, 3.6),
    Vector(-0.5, 2.0, 4.8),
    Vector(-2.4, -1.1, -0.9)
]

max_distance = 0
farthest_point = None

for vec in points_list:
    distance = abs(vec)
    if distance >= max_distance:
        max_distance = distance
        farthest_point = vec

print(farthest_point, max_distance)

masses = [10, 20, 30]
vectors = [Vector(1, 2, 3), Vector(2, 3, 6), Vector(3, 2, 1)]
combined_vector = sum(vec * mass for vec, mass in zip(vectors, masses)) * (1 / sum(masses))

print(combined_vector)
print(abs(vectors[0] @ vectors[1]))
print(vectors[0] * (vectors[1] @ vectors[2]))

greatest_perimeter = 0

for vec_a in points_list:
    for vec_b in points_list:
        for vec_c in points_list:
            perimeter = abs(vec_b - vec_a) + abs(vec_c - vec_b) + abs(vec_a - vec_c)
            greatest_perimeter = max(greatest_perimeter, perimeter)

print(greatest_perimeter)

largest_area = 0

for vec_a in points_list:
    for vec_b in points_list:
        for vec_c in points_list:
            area = 0.5 * abs((vec_b - vec_a) @ (vec_c - vec_a))
            largest_area = max(largest_area, area)

print(largest_area)
