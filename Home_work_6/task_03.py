# Принимает список имен сотрудников, возвращает словарь, ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

from itertools import groupby as gr


def create_dictionary(person):
    person_sort = sorted(person)
    person_gr = gr(person_sort, key=lambda x: x[0])
    result = {}
    for key, group in person_gr:
        result = {**result, **{key: list(group)}}
    return result


person = ['Иван', 'Николай', 'Наталья', 'Петр', 'Андрей', 'Антон', 'Илья', 'Федот',
          'Панкрат', 'Афанасий', 'Автандил', 'Анастасия', 'Владимир', 'Яков']

print('Отсортированные сотрудники:\n', create_dictionary(person))
