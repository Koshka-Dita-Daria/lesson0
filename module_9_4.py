import random
from random import choice
first = 'Мама мыла раму'
second = 'Рамена мало было'
a = list(map(lambda x, y: x == y, first, second))
print(a)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for i in data_set:
                if type(i) == str:
                    file.write(f"{i}\n")
                else:
                    file.write(f"{i}")
        return data_set
    return write_everything
class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
       return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
write = get_advanced_writer('example1.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
print(first_ball())
print(first_ball())
print(first_ball())