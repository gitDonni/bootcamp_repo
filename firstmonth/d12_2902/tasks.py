import random
import sys

#1

# import my_module


#2

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# other_names = random.choices(names, k = 4)
#
# print(other_names)


#3

# print(sys.platform)


#6

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# random.shuffle(names)
# team_one = names[0:3]
# team_two = names[3:6]
# team_three = names[6:9]
# team_four = names[9:]
# print('Команда 1: ', team_one)
# print('Команда 2: ', team_two)
# print('Команда 3: ', team_three)
# print('Команда 4: ', team_four)

#1


# print(sys.argv[:])

#2

# a = input('Введите первое значение: ')
# b = input('Введите второе значение: ')
#
# print(a, '= занимает', sys.getsizeof(a), 'байтов')
# print(b, '= занимает', sys.getsizeof(b), 'байтов')



#3


# n = int(input('Введите длину пароля: '))
# if n <= 0:
#     print('Длина пароля должна быть положительным числом.')
# else:
#     pass_simvols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#     password = ''.join(random.choice(pass_simvols) for i in range(n))
#     print(f'Сгенерированный пароль: {password}')


#4




# print('Выберите: 1 - Камень, 2 - Ножницы, 3 - Бумага')
# user_choice = input('Введите номер: ')
#
# computer_choice = str(random.randint(1, 3))
#
# print(f'Ваш выбор: {user_choice}')
# print(f'Выбор компьютера: {computer_choice}')
#
# if user_choice == computer_choice:
#     print('Ничья!')
# elif (user_choice == '1' and computer_choice == '2') or (user_choice == '2' and computer_choice == '3') or (user_choice == '3' and computer_choice == '1'):
#     print('Вы выиграли!')
# else:
#     print('Вы проиграли!')


#5


# import random
#
# even_number = random.randrange(6, 13, 2)
# print(f'Cлучайное четное число: {even_number}')
#
# five = random.randrange(5, 101, 5)
# print(f'Число, кратное пяти: {five}')


from datetime import datetime, timedelta

today = datetime.now()

after_1000 = today + timedelta(days=1000)

print(f"Через 1000 дней будет {after_1000.strftime('%A, %d %B %Y')}")
