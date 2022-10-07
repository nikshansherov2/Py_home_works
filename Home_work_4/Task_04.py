# Формирует случайным образом список коэффициентов (от 0 до 10)
# многочлена степени k, записывает в файл полученный многочлен.

from random import randint


def create_coefficients(degree):
    i = 0
    while degree >= 0:
        with open("polynomial.txt", "a", encoding="utf-8") as my_f:
            coefficient = randint(-10, 10)
            if coefficient == 0:
                degree -= 1
                continue
            elif coefficient > 0 and i == 0:
                coefficient_str = str(coefficient)
            elif coefficient > 0 and i > 0:
                coefficient_str = ' + ' + str(coefficient)
            elif coefficient < 0 and i == 0:
                coefficient_str = str(coefficient)
            elif coefficient < 0 and i > 0:
                coefficient_str = ' - ' + str(abs(coefficient))

            if degree == 0:
                my_f.write(f'{coefficient_str} = 0\n')
            elif degree == 1:
                my_f.write(f'{coefficient_str}*x')
            else:
                my_f.write(f'{coefficient_str}*x^{degree}')
            degree -= 1
            i += 1


create_coefficients(int(input('Введите степень многочлена: ')))
