import math

def square(s):

    if not isinstance(side, int):
        s = math.ceil(side)
    return s ** 2

# Функция с целым числом
side = 5
result = square(side)
print(f"Площадь квадрата со стороной {side}: {result}")

# Функция с нецелым числом
side = 5.5
result = square(side)
print(f"Площадь квадрата со стороной {side}: {result}")