class Car:

    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn_direction(self):
        print(f'Машина повернула {user_direction}')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)

    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость')
        else:
            print('Вы не превысили скорость')


class SportCar:
    pass

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)

    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость')
        else:
            print('Вы не превысили скорость')

class PoliceCar:
    pass


user_speed = int(input('Введите скорость автомобиля: '))
user_car_name = (input('Введите название автомобиля: '))
user_car_color = (input('Введите цвет автомобиля: '))
user_police = (input('Введите полицейский ли автомобиль (True или False): '))
user_direction = input('Введите куда повернула машина: ')

# РЕЗУЛЬТАТ ОТРАБОТКИ КЛАССА Car

a = Car(user_speed, user_car_color, user_car_name, user_police, user_direction)
a.go()
a.stop()
a.turn_direction()
a.show_speed()

# РЕЗУЛЬТАТ ОТРАБОТКИ КЛАССА TownCar

b = TownCar(user_speed, user_car_color, user_car_name, user_police, user_direction)
b.show_speed()

# РЕЗУЛЬТАТ ОТРАБОТКИ КЛАССА WorkCar

c = WorkCar(user_speed, user_car_color, user_car_name, user_police, user_direction)
b.show_speed()






