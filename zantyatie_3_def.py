def hello(name):
    return "Привет, " + name + "!"
hello_name = hello("Гоша")
print(hello_name)

def get_list(list):
    for elem in list:
        print(elem)

get_list(["Яблоко", "Банан", "Вишня"])

def demo(*args, **kwargs):
    print(args)
    print(kwargs)
demo(1, 2, 3, a=4, b=5)

def add(a: int, b:int) -> int:
    return a + b
add_res = add(1, 2)
print(add_res)
print(add(1, 2))
assert  add(1,2) == 3

def t_check(t):
    if t > 30:
        print("Жара")
    elif t > 20:
        print("Терпимо")
    else:
        print("Каеф")
t_check(14)


