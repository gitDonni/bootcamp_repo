# #1
# lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == lang1:
#         print('this languages is in list')
#         break
#     else:
#         break


#2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == 'php':
#         break
#     print(i)

#3
# a = 7
# b = 0
# while b < 5:
#     a = a * 7
#     b += 1
# print(a)

#4
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages[:]:
    i += 1
    print(i, languages)