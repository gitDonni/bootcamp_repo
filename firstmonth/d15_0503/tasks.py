# # 1
# def add(a, b, ):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a / b
#
#
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
#
# print(f"Сумма: {add(num1, num2)}")
# print(f"Разность: {subtract(num1, num2)}")
# print(f"Произведение: {multiply(num1, num2)}")
# print(f"Частное: {divide(num1, num2)}")


# 2


# def my_func(text):
#     count = 0
#     for i in text:
#         count += 1
#     return count
#
# text = input('Введите предложение: ')
#
# print(my_func(text))

# 3
#
# dict1 = {1: 'a', 2: 'b', 3: 'c'}
# dict2 = {4: 'd', 5: 'e', 6: 'f'}
#
#
# def dict_func(x, y):
#     x.update(y)
#     return x
#
#
# print(dict_func(dict1, dict2))

# 4


# def get_order():
#     current_order = []
#
#     while True:
#         print("Что вы хотите заказать? (Введите 'готово', чтобы завершить заказ.)")
#         order = input().lower()
#         current_order.append(order)
#         if order == "готово":
#             break
#     with open("/home/daniyar/Desktop/menu.txt", "w") as file:
#         for item in current_order:
#             file.write(item + "\n")
#
#     print("Ваш заказ сохранен в файле menu.txt. Приятного аппетита!")
#
#
# get_order()



#5

# def create_file(filename):
#
#     with open(user_input, "w") as file:
#         print(f'Файл {filename} успешно создан в текущей директории.')
#
#
# user_input = input('Введите имя файла: ')
# create_file(user_input)


#6
# def outter():
#     def inner():
#         print('Я вложенная фукция')
#     print('Я главная функция')
#     return inner()
#
#
# outter()



#7


# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# def dict_to_tuple(my_dict):
#     tup1 = tuple(my_dict.keys())
#     tup2 = tuple(my_dict.values())
#     return tup1, tup2
#
#
# print(dict_to_tuple(my_dict))
