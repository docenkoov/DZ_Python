import math

def square(side):
   
    if not isinstance(side, int):
        side = math.ceil(side)
    return side ** 2

# Тестируем функцию с целым числом
side = 5
result = square(side)
print(f"Площадь квадрата со стороной {side}: {result}")

# Тестируем функцию с нецелым числом
side = 5.5
result = square(side)
print(f"Площадь квадрата со стороной {side}: {result}")