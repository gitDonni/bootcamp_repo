# 0
# dates_of_birth = {3, 10, 11, 13, 31, 21, 1, 10, 3, 5, 6, 6}
# dates_of_birth.remove(6)
# print(dates_of_birth)


#2
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# difer = farm_2.difference(farm_1)
# print(difer)

#3
# some_set = {1, 2, 3, 4, 5}
# some_set.add(6)
# deleted = some_set.pop()
# print(some_set)
# print(deleted)


#10

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']
# print(menu)

#20

# set1 = {'add', 'update', 'intersection', 'remove', 'difference', 'intersection_update', 'clear', 'discard', 'pop'}
# set2 = {'clear', 'get', 'keys', 'values', 'items', 'update'}
#
# print('похожие методы:', set1.intersection(set2))


#31


# new_dict = {}
# for i in range(3):
#     username = input("Введите имя пользователя: ")
#     password = input("Введите пароль: ")
#     new_dict[username] = password
#
# print("Словарь с учетными данными пользователей:", new_dict)


#27

# dict1 = {'Билл': 'программист', 'Стив': 'маркетолог', 'Айжан': 'SMMщица', 'Вова': 'слесарь', 'Гульжан': 'дантист'}
#
# for name, pro in dict1.items():
#     print('Здравствуйте,', name, '! Прекрасная профессия', pro)



#22


# numbers = set()
#
# for i in range(10):
#     num = input(f'Введите число {i + 1}: ')
#     numbers.add(num)
#
# print('Введенные числа:', numbers)



#99


# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['besh_barmak'] = 130
# print(menu)
# menu['besh_barmak'] = 135
# print(menu)
# del menu['borsh']
# print(menu)


#11

south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']

list_countries = list(set(south_american_countries))

print(list_countries)


#101


# suitcase = []
# things = ['очки', 'плавки', 'крем', 'зонт', 'шляпа']
# suitcase.extend(things)
# print(suitcase)
# suitcase.pop()
# print(suitcase)


#001

farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
set1 = farm_1.intersection(farm_2)
print('Животные которые есть в обоих фермах: ', set1)
set2 = farm_1.difference(farm_2)
print('Животные которые есть в первой, но нет во второй: ', set2)
