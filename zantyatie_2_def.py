def hello(name):
    return "Привет, " + name + "!"

hello_name = hello("Гоша")
print(hello_name)

def get_list(list):
    for fruit in list:
        print(fruit)

get_list(["Яблоко", "Банан", "Вишня"])
