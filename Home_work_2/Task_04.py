# Принимает число N. Задает список, заполненный числами из промежутка [-N, N].
# Принимает 2 позиции элементов. Выводит произведение элементов на указанных позициях.

number = int(input('Введите число: '))
while True:
    position_1 = int(input('Введите позицию первого элемента: '))
    position_2 = int(input('Введите позицию второго элемента: '))
    if (position_1 <= number * 2 + 1 and position_1 > 0) and \
            (position_2 <= number * 2 + 1 and position_2 > 0):
        break
    else:
        print('Значение позиции вне диапазона! Попробуйте еще раз.')
        continue
numbers = list()
for i in range(number * 2 + 1):
    numbers.append(-number + i)
multiplication = numbers[position_1 - 1] * numbers[position_2 - 1]
print(numbers)
print('Произведение элементов на позициях ', position_1, ' и ',
      position_2, ' равно ', multiplication)
