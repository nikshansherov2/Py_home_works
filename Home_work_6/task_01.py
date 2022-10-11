# Формирует исходный список случайных двузначных чисел, выводит на экран
# список чисел, значение которых больше предыдущего (на основе исходного списка).

from random import randint as rnd


def create_list(number):
    list_start = [rnd(10, 100) for x in range(number)]
    return list_start


list_start = create_list(int(input('Введите длину списка: ')))
print('Первоначальный список из случайныx двузначных чисел:\n', list_start)
list_end = [list_start[i] for i in range(1, len(list_start)) if list_start[i] > list_start[i - 1]]
print('Список чисел, значения которых больше предыдущего:\n', list_end)
