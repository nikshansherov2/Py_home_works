# Генерирует текст из строки 'abc' случайным образом через пробел,
# удаляет из текста все слова, содержащие "абв".

from random import choices


# Формирует строку.
def create_text(number):
    str_1 = ' '.join([''.join(choices('abc', k=3)) for i in range(number)])
    return str_1


str_begin = create_text(int(input('Введите количество подстрок: ')))
print('Сгенерированный текст:\t', str_begin)
str_end = str_begin.replace('abc', '')
print('Текст без "авс":\t\t', str_end.replace('  ', ' '))
