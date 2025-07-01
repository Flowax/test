text = "Тестовый текст"
print(text)
print(text[0:6])
print(text[-13])
print(len(text))

print(text.upper())
print(text.title())

bad_text = "    hello world!   "
print(bad_text.lstrip())
print(bad_text.rstrip())

new_text = text.replace("текст", "привет")
print(new_text)

words = text.split()
print(words)

print(text.islower())

name = "george"
age = "25"
city = "NN"
# Старый способ %
#print("Имя: %s, Возраст: %d, Город: %s" % (name, age, city))

# format
print("Имя: {} Возраст: {}, Город: {}".format(name, age, city))