# Сжимает данные из файла no_compress.txt, записывает их в файл compress.txt.
# Восстанавливает данные из compress.txt и выводит их на экран.

from module import compress_file, decompress_file

compress_file('no_compress.txt')
print('Восстановленные данные:\n' + decompress_file())
