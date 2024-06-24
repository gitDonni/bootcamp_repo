import json
from pprint import pprint
# first = {'login': 'qwerty', 'email': 'qwerty@gmail.com', 'age': 30, 'phone_number': 996550123321}
# second = {'login': 'ytrewq', 'email': 'ytrewq@gmail.com', 'age': 20, 'phone_number': 996700321123}
# third = {'login': 'qazxsw', 'email': 'qazxsw@gmail.com', 'age': 25, 'phone_number': 996770132312}
#
# lst_users = [first, second, third]
#
# with open('users.json', 'w') as file:
#     json.dump(lst_users, file, indent=4)


with open('users.json', 'r') as file:
    data = json.load(file)
    for i in data:
        i['language'] = 'KG'

with open('users.json', 'w') as upd_file:
    json.dump(data, upd_file, indent=4)
pprint(data)