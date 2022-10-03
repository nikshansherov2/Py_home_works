# Создает список случайных чисел. Перемешивает список.
# Выводит на экран первоначальный и перемешанный списки.

import random

numbers = list()
length = int(input('Введите длину списка: '))
for i in range(length):
    numbers.append(random.randint(0, 100))
print('Первоначальный список = ', numbers)
n = len(numbers)
while n > 0:
    index = random.randint(0, n - 1)
    temp = numbers.pop(index)
    numbers.append(temp)
    n -= 1
print('Перемешанный список = ', numbers)
