class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки {self.title}')
class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


a = Stationery('1')
a.draw()
b = Pen('2')
b.draw()
c = Pencil('3')
c.draw()
d = Handle('4')
d.draw()