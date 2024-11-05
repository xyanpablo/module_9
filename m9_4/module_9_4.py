import random
from random import choice
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='UTF-8') as file:
            for i in data_set:
                file.write(str(i) + '\n')
    return write_everything

class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        return random.choice(self.words)


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())