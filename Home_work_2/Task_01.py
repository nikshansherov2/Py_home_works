# Принимает на вход вещественное число и показывает сумму его цифр.

number = str(input('Введите число: '))
length = len(number)
number = float(number)
if number < 0:
    number *= -1
number = number * 10 ** (length - 2)
sum = 0
while number > 0:
    sum += number % 10
    number = number // 10
print('Сумма цифр в введенном числе = ', sum)
