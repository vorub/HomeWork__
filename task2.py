class Road:

    def __init__(self, _length, _width):
        self._width = _width
        self._length = _length
        self.thickness = int(input('Введите число см толщины полотна: '))
        self.weigth = int(input('Введите массу асфальта для покрытия одного кв метра дороги асфальтом: '))

    def asphalt_weight(self):
        mass = self.thickness * self._width * self.weigth * self._length
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {mass}')

a = Road(100, 100)
a.asphalt_weight()







