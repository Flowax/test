# Список list

numbers = [1, 2, 3, 4, 5]
print(numbers[0])
print(numbers[-1])
print(numbers.index(4))
numbers.append(6)
numbers.insert(5, 6)
print(numbers)


# кортежи (tuple)
coordinate = (10.0, 20.0, 20.0)
print(coordinate[1])
print(coordinate.count(20.0))
print(coordinate.index(20.0))

#Множества (set)
unic_num = {1, 2, 2, 3, 3}
print(unic_num)

# словарь (dict)
person = {
    "name": "George",
    "age": "26",
    "city": "NN"
}
print(person)
print(person.keys())
print(person.values())
print(person.get("name"))
print(person.get("email", "email Отсутствует"))
person.update({"age": 30, "email": "george@gmail.com"})
print(person)
print(person.get("email", "email Отсутствует"))

if "city" in person:
    print("Город: ", person["city"])

for key, value in person.items():
    print(f"{key.upper()}: {value}")

del person["email"]
print(person)

def print_data(number, coor, unic_id, pers_info):
    print("Числа")
    for i, num in enumerate(num):
        print(f"{i + 1}, {num}")
    print("Координаты;")
    print(f"X: {coor[0]}, Y: {coor[1]}")
    print("Уникальные значения:")
    for uid in unic_id:
        print(f"{uid}")
    print("Инфа о челе:")
    for key, value in person.items():
        print(f"{key}: {value}")


