import io
from pprint import pprint
def custom_write(file_name, *strings):
    strings_positions = set()
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        if i not in strings_positions:
            strings_positions["{tuple(i, int(file.tell()))}"].append(i)
            file.write(f'{i}\n')
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