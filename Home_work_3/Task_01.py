# Создает список длиной заданной пользователем.
# Находит сумму элементов списка, стоящих на нечётных позициях.

from random import randint


# Создает список случайных элеметов, находит сумму элементов на нечетных позициях.
def find_sum(n):
    sum = 0
    my_list = []
    for i in range(n):
        my_list.append(randint(0, 100))
    print('Сформированный список: ', my_list)
    for i in range(0, n, 2):
        sum += my_list[i]
    return sum


number = int(input('Введите длину списка: '))
print('Сумма элементов, стоящих на нечетных позициях равна ', find_sum(number))
