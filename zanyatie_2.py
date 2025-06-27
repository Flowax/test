import random
import string

for num in range(10):
    if num == 2:
        continue
    if num == 4:
        pass
    if num == 7:
        break
    print(num)

fruits=["Яблоко","Банан", "Вишня"]
for fruit in fruits:
    if fruit == "Банан":
        continue
    print(fruit)

count = 0
while count < 3:
    print(count)
    count += 1

"""while True:
    answer = input("Продолжить? (д/н): ")
    if answer.lower() == "н":
        break
"""
"""
Цели циклов
"""
#1. Перебор
for fruit in fruits:
    print(fruit)

#Строчный перебор
for char in "Python":
    print(char)

# 2. Повторы
for _ in range(10):
    print("Привет!")

# Счетчик
for i in range(1,11):
    print(f"{i}, привет")

# 3. Обработка ввода
#age = input("Сколько теле лет? ")
#while not age.isdigit():
#    age = input("Сколько теле лет? ")

# 4. Автоматизация
numbers = [1, 4, 7, 10]
for n in numbers:
    if n % 2 == 0:
        print(n)
# Подсчет
total = 0
for n in numbers:
    total += n
print(total)

#Генерация через циклы
for _ in range(10):
    password = ""
    for _ in range(8):
        password += random.choice(string.ascii_letters + string.digits)
    print("Пароль: ", password)
