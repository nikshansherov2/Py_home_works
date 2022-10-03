# Формирует список из произвольных вещественных чисел, длиной, заданной пользователем.
# Находит разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform


# Создает список случайных элеметов, формирует список из
# дробных частей элементов первоначального списка.
def create_list(number):
    my_list = []
    for i in range(number):
        my_list.append(round(uniform(0, 10), 2))
    print('List: ', my_list)
    my_list_dif = []
    for i in range(number):
        my_list_dif.append(my_list[i] % 1)
    return my_list_dif


number = int(input('Enter the length of the list: '))
my_list = create_list(number)
min_list = round(min(my_list), 2)
max_list = round(max(my_list), 2)
difference = round(max_list - min_list, 2)
print('Min = ', min_list, ' Max = ', max_list, ' Difference = ', difference)
