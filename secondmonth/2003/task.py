import json

def load_from_file(file):
    with open(file, 'r') as file:
        cities = json.load(file)
    return cities

def save_to_file(file, cities):
    with open (file, 'w') as file:
        json.dump(cities,file)

def add(new_city, cities):
    if new_city in cities:
        print(f'Такой город уже есть в списке: {cities.index(new_city)+1}. {new_city}')
    else:
        cities.append(new_city)
    print('Город добавлен')

def show(cities):
    for i, j in enumerate(cities, start=1):
       print(i, j)

def replace(new_city, old_city, cities):
    if new_city in cities:
        print(f'Такой город уже есть в списке: {cities.index(new_city)+1}. {new_city}')
    elif old_city not in cities:
        print('Город отсутутвтет')
    elif old_city in cities:
        cities.remove(old_city)
        cities.append(new_city)
        print('Город заменен')

def delete(cities, user_input):
    if user_input not in cities:
        print('Текущий город оттсутвтвует')
    else:
        cities.remove(user_input)
        print('Город удален')

cities = load_from_file('cities.json')

while True:
    print('''
    Выберите действие:
    1. Добавить новый город
    2. Отобразить список городов
    3. Заменить город
    4. Удалить город
    5. Выход
    ''')
    choice = input('Ваше действие: ')
    if choice == '1':
        new_city = input('Введите название города - ')
        add(new_city, cities)
        save_to_file('cities.json', cities)
    if choice == '2':
        show(cities)
    if choice == '3':
        old_city = input('Текущий город - ')
        new_city = input('Новый город - ')
        replace(new_city, old_city, cities)
        save_to_file('cities.json', cities)
    if choice == '4':
        user_input = input('Введите название города - ')
        delete(cities, user_input)
        save_to_file('cities.json', cities)
    if choice == '5':
        save_to_file('cities.json', cities)
        print('Программа завершена')
        break
