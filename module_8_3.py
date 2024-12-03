class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True


    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumber('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumber('Неверная длина номера')
        return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message

def create_car(model, vin, numbers):
    try:
        car = Car(model, vin, numbers)
    except IncorrectCarNumber as inc_num:
        print(f'Error {inc_num.message}')
    except IncorrectVinNumber as inc_vin:
        print(f'Error {inc_vin.message}')
    else:
        print(f'{car.model} успешно создан!')

create_car('Toyota', 8746122, 'y685ma')
create_car('Aston Martin', 12948277, 'k155na')
create_car('Porsche', 2948277, 'k155n')


