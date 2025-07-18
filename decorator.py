import time


def my_dec(func):
    def wrapper():
        print("Начало")
        func()
        print("Конец")
    return wrapper

@my_dec
def hello_world():
    print("Привет")

hello_world()

def time_dec(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Начало в {start_time}, конец в {end_time}")
    return wrapper

@time_dec
def operation():
    print("ыыы")
    time.sleep(3)
    print("333")

operation()