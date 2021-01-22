class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        worker_name = self.name + ' ' + self.surname
        print(f'Полное имени сотрудника: {worker_name}')

    def get_total_income(self):
        worker_income = self._income['wage'] + self._income['bonus']
        print(f'Доход с учетом премии: {worker_income}')


user_name = input('Введите имя сотрудника: ')
user_surname = input('Введите фамилию сотрудника: ')
user_position = input('Введите должность сотрудника: ')
user_wage = int(input('Введите доход сотрудника: '))
user_bonus = int(input('Введите премию сотрудника: '))
a = Position(user_name, user_surname, user_position, user_wage, user_bonus)
a.get_full_name()
a.get_total_income()

