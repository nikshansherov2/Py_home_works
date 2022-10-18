# Проверяет на целое и на существование файла

import os.path


# Проверка на целое
def exc_quantity():
    while True:
        try:
            n = int(input('Для создания телефонного справочника введите количество человек: '))
            return n
        except ValueError:
            print('Ошибка ввода! Побробуйте еще раз.')
            continue


# Проверка существования файла
def exc_file(file_name):
    if os.path.exists(file_name):
        return True
    else:
        return False
