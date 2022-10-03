# Преобразует десятичное число в двоичное.

# Преобразует целую часть числа.
def convert_to_binary_int(number_int):
    list_binary_int = []
    while number_int:
        list_binary_int.insert(0, number_int % 2)
        number_int //= 2
    return list_binary_int


# Преобразует дробную часть числа.
def convert_to_binary_float(number_float):
    list_binary_float = []
    i = 0
    while number_float != 0 and i < 5:
        list_binary_float.append(int(number_float * 2))
        number_float = number_float * 2 % 1
        i += 1
    return list_binary_float


number = float(input('Введите число: '))
if number % 1 == 0:
    number = int(number)
    number_int = convert_to_binary_int(number)
    print('Число в двоичном виде равно: ' + "".join(map(str, number_int)))
else:
    number_int = int(number)
    number_float = number % 1
    number_int = convert_to_binary_int(number_int)
    number_float = convert_to_binary_float(number_float)
    print('Число в двоичном виде равно: ' + "".join(map(str, number_int)) + '.'
          + "".join(map(str, number_float)))
