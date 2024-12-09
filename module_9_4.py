import random

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

lamfunc = lambda a, b: a == b
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='UTF-8') as file:
            file.write(data_set.__str__())
    return write_everything


first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lamfunc, first, second)))

write = get_advanced_writer('Products.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('sd', 'gwe', 'tv')
print(first_ball())
print(first_ball())
print(first_ball())