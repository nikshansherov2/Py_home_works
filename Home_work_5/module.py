# Здесь находятся функция сжатия данных (compress_file)
# и функция восстановления данных (decompress_file).

def compress_file(a):
    with open(a, 'r') as f:
        lines_n_c = f.readlines()
    str_comp = ''
    for i in range(len(lines_n_c)):
        k = 1
        for j in range(len(lines_n_c[i]) - 1):
            if lines_n_c[i][j] != lines_n_c[i][j + 1]:
                str_comp = str_comp + ''.join(str(k) + ''.join(lines_n_c[i][j]))
                k = 1
            else:
                k += 1
        str_comp += '\n'
    with open('compress.txt', "w", encoding="utf-8") as f:
        f.write(str_comp)


def decompress_file():
    with open('compress.txt', 'r') as f:
        lines = f.readlines()
    str_decomp = ''
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '\n':
                str_decomp += ''.join(lines[i][j])
            elif j % 2 == 0:
                str_decomp += int(lines[i][j]) * lines[i][j + 1]
            else:
                continue
    return str_decomp
