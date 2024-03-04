#1

# import my_module


#2

# import random

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# other_names = random.choices(names, k = 4)

# print(other_names)


#3

# import sys
# print(sys.platform)


#6
# import random

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# random.shuffle(names)
# team_one = names[0:3]
# team_two = names[3:6]
# team_three = names[6:9]
# team_four = names[9:]
# print('Команда 1: ',team_one)
# print('Команда 2: ',team_two)
# print('Команда 3: ',team_three)
# print('Команда 4: ',team_four)

#1

# import sys

# print(sys.argv[:])

#2

import sys

a = input('Введите первое значение ')
b = input('Введите второе значение ')

print(a, '= занимает', sys.getsizeof(a), 'байтов')
print(b, '= занимает', sys.getsizeof(b), 'байтов')