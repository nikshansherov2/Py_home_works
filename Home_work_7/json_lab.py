# Производит запись в файл json и чтение из файла json

import json


# Запись в файл
def write(n):
    l = n[0]
    file_name = n[1]
    with open(file_name, 'w', encoding="utf-8") as f:
        json.dump(l, f, ensure_ascii=False, indent=4)


# Чтение из файла
def read(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        l = json.load(f)
        return l
