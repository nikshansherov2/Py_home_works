# Производит запись в файл csv и чтение из файла csv

import csv


# Запись в файл
def write(n):
    l = n[0]
    file_name = n[1]
    with open(file_name, 'a', encoding='utf-8') as f:
        f_w = csv.writer(f)
        f_w.writerows(l)


# Чтение из файла
def read(file_name):
    with open(file_name, 'r') as f:
        l = []
        f_r = csv.reader(f)
        for row in f_r:
            l.append(row)
        return l
