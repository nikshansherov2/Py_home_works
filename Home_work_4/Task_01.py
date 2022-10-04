# Вычислить число c заданной точностью d

def round_number(number, accuracy):
    number = round(number, accuracy)
    return number


number = float(input('Введите число для округления: '))
accuracy = int(input('Введите количество знаков для округления: '))
print('Округленное число:', round_number(number, accuracy))
