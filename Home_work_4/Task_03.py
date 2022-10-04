# Формирует случайную последовательность чисел. Выводит список неповторяющихся
# элементов исходной последовательности в том же порядке.

from random import randint


def create_initial_list(number):
    initial_list = []
    for i in range(number):
        initial_list.append(randint(0, 10))
    print('Первоначальный список: ', initial_list)
    return initial_list


def create_list(initial_list):
    my_list = []
    for value in initial_list:
        if initial_list.count(value) == 1:
            my_list.append(value)
    print('Новый список:', my_list)


initial_list = create_initial_list(int(input('Введите длину списка: ')))
create_list(initial_list)
