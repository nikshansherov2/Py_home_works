# Вычислить число c заданной точностью d

def round_number(number, accuracy):
    print(f'{number:.{accuracy}f}')
#    return number


number = float(input('Введите число для округления: '))
accuracy = int(input('Введите точность вычисления: '))
round_number(number, accuracy)