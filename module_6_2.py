class Vehicle:
    __COLOR_VARIANTS = ['лавандовый', 'бордовый', 'телесный']

    def __init__(self, name, model, engine_power, color):
        self.owner = name
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        if Vehicle.__COLOR_VARIANTS.__contains__(new_color.lower()):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    def print_info(self):
        print(f'Модель: {self.get_model()}')
        print(f'Мощность двигателя: {self.get_horsepower()}')
        print(f'Цвет: {self.get_color()}')
        print(f"Владелец: {self.owner}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, name, model, engine_power, color):
        super().__init__(name, model, engine_power, color)

vehicle1 = Sedan('Конь', 'Ford Mustang', 99, 'Лавандовый')
vehicle1.print_info()

vehicle1.set_color('БеЛый')
vehicle1.set_color('БОрдовыЙ')
vehicle1.owner = 'Осел'

vehicle1.print_info()
