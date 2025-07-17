import os

a = 5
b = 0

try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Делить на ноль нельзя!")

try:
    result = 10 / a
except ValueError:
    print("Не число")
except ZeroDivisionError:
    print("Делить на ноль нельзя!")

current_dir = os.getcwd()
print(current_dir)