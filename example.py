name = "George"
age = 26
height = 1.79
human = True
print(name)

name_2: str = "Gosha"
age_2: int = 26
height_2: float = 1.79
human_2: bool = True
print(f"Имя: {name_2}, Возраст: {age_2}")
print(type(name_2))
print(type(age_2))


a = 10
b = 5

# Арифметика
c = a + b
print(c)
print(a - b)
print(a / b)
print(a * b)
print(a % b)

#Сравнения
print(a == b)
print(a != b)
print(a > b)
print(a <= b)

x = True
y = False
print(f"Сравнение:{x == y}")

"""
Условные конструкции IF, ELIF, ELSE
"""

t = 25

if t > 30:
    print("Жара")
elif t > 20:
    print("Терпимо")
else:
    print("Каеф")


status = "Студент" if age > 18 else "Школяр"
print(status)

is_student = True
if is_student:
    print("Он студент")
else:
    print("Он школяр")