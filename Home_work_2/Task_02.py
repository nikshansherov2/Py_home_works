# Принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = int(input('Введите число: '))
numbers = list()
for i in range(1, number + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    numbers.append(factorial)
print('Набор произведений чисел от 1 до введенного числа:')
print(numbers)
