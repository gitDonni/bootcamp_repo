#1

# x = 2 ** 3
# y = 3 ** 2
#
# if x > y:
#     print("Значение переменной X больше, чем Y:", x)
# else:
#     print("Значение переменной Y больше, чем X:", y)


# #2
# a = int(input('первое:'))
# b = int(input('второе:'))
# c = int(input('третье:'))
#
# if a <= b and a <= c:
#     print('первое самое маленькое')
# elif b <= a and b <= c:
#     print('второе самое маленькое')
# else:
#     print('третье самое маленькое')
#
# if a >= b and a >= c:
#     print('первое самое большое')
# elif b >= a and b >= c:
#     print('второе самое большое')
# else:
#     print('третье самое большое')

#3
# a = 17931 % 17
# b = 546 % 17
# c = 934 % 17
#
# if a <= b and a <= c:
#     print('остаток меньше в = a')
# elif b <= a and b <= c:
#     print('остаток меньше в = b')
# elif c <= a and c <= b:
#     print('остаток меньше в = c')


#4
# x = 13
# y = x ** 2
# z = 172
#
# if y < z:
#     y = y ** 2
#     print('13 в квадрате меньше', z, 'поэтому 13 в кубе =', y)
#
# else:
#     print('13 в квадрате больше', z, 'поэтому возводим в квадрат один раз')


#5


# num = int(input('Введите число:'))
# if num % 2 == 0:
#     print("Число чётное.")
# else:
#     print("Число нечётное.")
#
# if num % 3 == 0:
#     print("Число делится на 3 без остатка.")
# else:
#     print("Число не делится на 3 без остатка.")
#
# if num ** 2 > 1000:
#     print("Число после возведения в квадрат больше 1000.")
# else:
#     print("Число после возведения в квадрат не больше 1000.")


#6

# num = int(input('Введите число:'))
#
# if 0 <= num <= 21 or 57 <= num <= 100:
#     print("Число находится в разрешенном диапазоне.")
# else:
#     print("Число не находится в разрешенном диапазоне.")

#7

# if True:
#     print("Это условие всегда срабатывает.")


#8

# x = 10
#
# if x > 5:
#     print("x больше 5")
#     if x > 7:
#         print("x также больше 7")
#         if x > 8:
#             print("x опять больше 8")
#         else:
#             print("x не больше 8")
#     else:
#         print("x не больше 7")
# else:
#     print("x не больше 5")


#9


# a = 10//5
# b = 10/5
#
# if a == b:
#     print(a+b)
# else:
#     print('Они не равны')


#11


# a = 10
# b = 5
#
# if 0 < a and 0 < b:
#     print('a и b положительные числа')
# else:
#     print('a и b не положительные числа')


#12


a = 10
b = 5

if a > b:
    print('a+2')
else:
    print('b+2')
