# Принимает на вход вещественное число и показывает сумму его цифр.
# Вариант 2.

number = str(input('Введите число: '))
number = number.replace('.', '')
number = int(number)
if number < 0:
    number *= -1
sum = 0
while number > 0:
    sum += number % 10
    number = number // 10
print('Сумма цифр в введенном числе = ', sum)
