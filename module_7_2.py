import io
from pprint import pprint
def custom_write(file_name, *strings):
    file_name = 'text.txt'
    file = open(file_name, 'a')
    i = 0
    for line in strings:
        i += 1
        file.write(f'{str(line)}\n')
        print(i, file.tell(), line)
    file.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
