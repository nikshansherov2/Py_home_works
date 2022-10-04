# Принимает натуральное число N. Выводит на экран список
# простых множителей числа N.

def multipliers(n):
    mult = 2
    mult_list = []
    while mult * mult <= n:
        if n % mult == 0:
            mult_list.append(mult)
            n //= mult
        else:
            mult += 1
    if n > 1:
        mult_list.append(n)
    return mult_list


number = int(input('Введите натуральное число: '))
print('Список простых множителей числа', number, ':', multipliers(number))
