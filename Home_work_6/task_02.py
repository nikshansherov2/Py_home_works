# Выводит на экран числа от 20 до N, кратные 20 или 21.

number = int(input('Введите число: '))
list_end = [n for n in range(20, number + 1) if n % 20 == 0 or n % 21 == 0]
print('Список значений кратных 20 и 21:\n', list_end)
