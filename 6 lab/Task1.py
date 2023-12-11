class ComplexNumber:
  
    def __init__(self, real: float, imaginary: float) -> None:
        self.real = real
        self.imaginary = imaginary
    
    def __str__(self) -> str:
        if self.imaginary == 0:
            return f"{self.real}"
        sign = '+' if self.imaginary > 0 else ''
        return f"{self.real}{sign}{self.imaginary}i"
        
    def __add__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    
    def __mul__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)
    
    def __truediv__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        denominator = other.real ** 2 + other.imaginary ** 2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real_part, imaginary_part)

    def __abs__(self) -> float:
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

first_complex = ComplexNumber(3, 4)
second_complex = ComplexNumber(2, -1)

print(first_complex + second_complex)
print(first_complex - second_complex)
print(first_complex * second_complex)
print(first_complex / second_complex)
print(abs(first_complex))
