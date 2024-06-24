#1
# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
#
# results = []
#
# for item in values:
#     try:
#         set(item)
#         results.append(True)
#     except TypeError:
#         results.append(False)
# can_convert = all(results)
#
# print(f'Можно ли конвертировать values в SET? {can_convert}')


#2

# numbers = set()
#
# for i in range(5):
#     num = int(input('Введите целое число: '))
#     numbers.add(num)
#
# min_num = min(numbers)
# print(f'Самое маленькое число: {min_num}')



#4

# try:
#     zaim = float(input('Введите сумму займа: '))
#     if zaim < 50000:
#         print('Сумма займа должна быть не менее 50,000. Пожалуйста, попробуйте снова.')
#
#     procent = 3.47
#     interest_decimal = procent / 100
#
#     pereplata = zaim * (procent / 100)
#     result = zaim + pereplata
#
#     pereplata_r = round(pereplata, 2)
#     result_r = round(result, 2)
#
#     print(f'Переплата по кредиту: {pereplata_r} сом')
#     print(f'Итоговая сумма к возврату: {result_r} сом')
#
# except ValueError:
#     print('Некорректный ввод. Пожалуйста, введите число.')

#5

#TypeError
# x = '2'
# y = 2
# result = x + y

#IndexError
# my_list = [1, 2, 3]
# element = my_list[10]

# #NameError
# print(prosto_print)



#7

# lst = []
#
# for i in range(10):
#     lst.append(i)
#
# a = list(reversed(lst))
# sls_obj = slice(0, 8)
# print(a[sls_obj])


#8
# try:
#     a = 0
#     b = 1
#     numbers = []
#     while b > a:
#         numbers += b
#         b += 1
# except TypeError:
#     print('Ошибка!!! Разные типы данных')



#9
dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}

for x in dict_.keys():
    try:
        x + 'abc'
    except TypeError:
        print(f"Ключ '{x}' не является строковым значением")
