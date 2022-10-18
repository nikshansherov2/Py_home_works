# Основной интерфейс программы
import csv_lab, json_lab
import exceptions


# Создает список для файла csv
def create_list():
    n = exceptions.exc_quantity()
    people = []
    for i in range(n):
        temp = []
        temp.append(input(f'Введите фамилию {i + 1} человека: '))
        temp.append(input(f'Введите имя {i + 1} человека: '))
        temp.append(input(f'Введите телефон {i + 1} человека: '))
        temp.append(input(f'Введите справку на {i + 1} человека: '))
        people.append(temp)
    file_name = input('Введите имя файла для сохранения результатa: ') + '.csv'
    return people, file_name


# Создает словарь для файла json
def create_dict():
    n = exceptions.exc_quantity()
    people = {}
    people['люди'] = []
    for i in range(n):
        temp = {}
        temp['фамилия'] = input(f'Введите фамилию {i + 1} человека: ')
        temp['имя'] = input(f'Введите имя {i + 1} человека: ')
        temp['телефон'] = input(f'Введите телефон {i + 1} человека: ')
        temp['описание'] = input(f'Введите справку на {i + 1} человека: ')
        people['люди'].append(temp)
    file_name = input('Введите имя файла для сохранения результатa: ') + '.json'
    return people, file_name


# Выбор действия
def select_action():
    print('Выберите действие:\nзаписать в файл - 1\nсчитать из файла - 2')
    while True:
        try:
            action = int(input('Введите выбранное действие: '))
            if 0 < action <= 2:
                return action
            else:
                print('Значение вне диапазона! Побробуйте еще раз.')
                continue
        except ValueError:
            print('Это не цифра! Побробуйте еще раз.')
            continue


# Выбор файла для чтения
def select_file_read():
    print('Введите тип файла, который хотите считать:\n1 - csv\n2 - json')
    while True:
        try:
            n = int(input('Ввод: '))
            if 0 < n <= 2:
                break
            else:
                print('Значение вне диапазона! Попробуйте еще раз.')
        except ValueError:
            print('Это не цифра! Побробуйте еще раз.')
            continue
    if n == 1:
        while True:
            file_name = input('Введите имя файла: ') + '.csv'
            if exceptions.exc_file(file_name):
                l = csv_lab.read(file_name)
                break
            else:
                print('Такого файла не существует! Попробуйте еще раз.')
                continue
        print(f'Содержимое файла {file_name}:\n', l)
    else:
        while True:
            file_name = input('Введите имя файла: ') + '.json'
            if exceptions.exc_file(file_name):
                l = json_lab.read(file_name)
                break
            else:
                print('Такого файла не существует! Попробуйте еще раз.')
                continue
        print(f'Содержимое файла {file_name}:\n', l)


# Выбор типа файла для записи
def select_file_type():
    print('Выберите тип файла в который вы хотите сохранить Ваш телефонный справочник: ')
    print('Введите 1 - если csv\nВведите 2 - если json')
    while True:
        try:
            n = int(input('Введите цифру вашего выбора: '))
            if 0 < n <= 2:
                return n
            else:
                print('Значение вне диапазона! Побробуйте еще раз.')
                continue
        except ValueError:
            print('Это не цифра! Побробуйте еще раз.')
            continue


print('Вас приветствует программа - создание телефонного справочника !')
if select_action() == 1:
    n = select_file_type()
    if n == 1:
        csv_lab.write(create_list())
    if n == 2:
        json_lab.write(create_dict())
else:
    select_file_read()
