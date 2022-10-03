# Получает на вход чило N, формирует список из N чисел, заполненный по формуле
# (1 + 1/n) ** n и вывoдит на экран их сумму.

number = int(input('Введите число: '))
numbers = list()
sum = 0
for i in range(1, number + 1):
    numbers.append(round((1 + 1 / i) ** i))
    sum += numbers[i - 1]
print(numbers)
print(sum)
