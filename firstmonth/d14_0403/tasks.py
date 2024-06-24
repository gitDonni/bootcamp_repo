#1

# list_number = [1, 'dva', 'three', 4, 'five', 'shest']
#
# def list_popolam():
#     new_list = list_number[0:len(list_number) // 2]
#     new_list2 = list_number[len(list_number) // 2:]
#     new_list = new_list[::-1]
#     new_list2 = new_list2[::-1]
#     new_list.extend(new_list2)
#     print(new_list)
# list_popolam()


#2

# def fibonacci():
#     a = 0
#     b = 1
#     for i in range(10):
#         a = b
#         b = a + b
#         print(b, end=',')
#
# fibonacci()

#3
# def slojenie(a, b):
#     return a + b
#
# def vichitanie(a, b):
#     return a - b
#
# def calc(a, b):
#     summa = slojenie(a, b)
#     razn = vichitanie(a, b)
#     return summa, razn
#
#
# x = 10
# y = 5
# summa, razn = calc(x, y)
# print(f'Сумма: {summa}, Разность: {razn}')


#4

# def create_file():
#     filename = input('Введите имя файла: ')
#     try:
#         with open(filename, "w") as file:
#             pass
#         print(f"Файл '{filename}' успешно создан.")
#     except OSError:
#         print(f"Не удалось создать файл '{filename}'.")
#
#
# my_function = create_file
#
# my_function()

#5
# import random
#
#
# def gen_number():
#     digits = [random.choice([1, 4, 5, 7, 9, 0]) for i in range(6)]
#
#     number = '0444' + ''.join(map(str, digits))
#     return number
#
#
# print(gen_number())
# print(gen_number())
# print(gen_number())
