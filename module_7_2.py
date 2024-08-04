import io
from pprint import pprint
def custom_write(file_name, *strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = set()
    k = 1
    for i in strings:
        file.write(f'{i}\n')
        strings_positions["tuple(i, int(file.tell())"] = i
        k += 1
        file.seek(0)
    file.close

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
