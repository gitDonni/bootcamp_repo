#1
# lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == lang1:
#         print('this languages is in list')


# 2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == 'php':
#         break
# print('дoшёл до php')

# 3
# a = 7
# b = 0
# while b < 5:
#     a = a * 7
#     b += 1
# print(a)

# 4
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i, lang in enumerate(languages):
#     print(i, lang)


#5

# for i in range(1, 11):
#     print(i, end=",")
# for i in range(9, 0, -1):
#     print(i, end=",")
# print(1)


#6

# names = ('Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай', 'Салават', 'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек', 'Дастан', 'Бекмамат', 'Аслан')
#
# for i, name in enumerate(names):
#     if i % 2 == 0:
#         print(name)


#7

# names = ('Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай', 'Салават', 'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек', 'Дастан', 'Бекмамат', 'Аслан')
#
# for i in range(1, len(names), 2):
#     print(names[i])

#8

# num = int(input("Введите число: "))
#
# if 100 <= num <= 999:
#     print("Число трёхзначное")
# else:
#     print("Число не трёхзначное")
#
# if num > 0 or num % 2 == 0:
#     print("Число либо положительное, либо чётное")
# else:
#     print("Число не положительное и чётное ")
#
# if num % 31 == 0:
#     print("Число делится на 31 без остатка")
# else:
#     print("Число не делится на 31 без остатка")
#
# if (num > 100 and num % 17 == 0) or num == 169:
#     print(f"Это число: {num}")


#9


start_num = -100
end_num = 100
uslovie1 = 0
uslovie2 = 0
for num in range(start_num, end_num + 1):
    if num % 13 == 0 and num % 2 == 0:
        num = num ** 2
        print(num)

    if (num - start_num) % 7 == 0:
        if num % 2 != 0:
            print(num)


for num in range(start_num, end_num + 1):
    if num % 13 == 0 and num % 2 == 0:
        uslovie1 += 1
    if (num - start_num) % 7 == 0:
        if num % 2 != 0:
            uslovie2 += 1

print('Чисел, подходящих под первое условие:', uslovie1)
print('Чисел, подходящих под второе условие:', uslovie2)
