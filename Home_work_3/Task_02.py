# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint


# Создает список случайных элеметов.
def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(randint(0, 10))
    print('Сформированный список: ', my_list)
    return my_list


# Создает список произведений пар чисел.
def find_list(my_list):
    n = len(my_list)
    my_list_2 = []
    for i in range(n // 2):
        my_list_2.append(my_list[i] * my_list[n - 1 - i])
    if n % 2 != 0:
        my_list_2.append(my_list[n // 2])
    return my_list_2


number = int(input('Введите длину списка: '))
my_list = create_list(number)
print('Список произведений пар чисел: ', find_list(my_list))
