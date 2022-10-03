# Создает список чисел Фибоначчи, в том числе для отрицательных индексов.

# Формирует список из чисел Фибоначчи.
def fibonacci_list(number):
    fib_list = []
    for i in range(number + 1):
        if i == 0:
            fib_list.append(i)
        elif i == 1:
            fib_list.append(i)
            fib_list.insert(0, i)
        else:
            fib_list.append(fib_list[-1] + fib_list[-2])
            fib_list.insert(0, fib_list[1] - fib_list[0])
    return fib_list


number = int(input('Введите число: '))
print('Список чисел Фибоначчи: ', fibonacci_list(number))
