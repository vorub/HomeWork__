class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        import time
        print('красный')
        time.sleep(7)
        print('желтый')
        time.sleep(2)
        print('зеленый')
        time.sleep(7)

traffic_light = TrafficLight()
traffic_light.running()







