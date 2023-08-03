 
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Autobus(Transport):
    def __init__(self,name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
    def appellation (self):
        print(f'Название автомобиля:{self.name},Скорость:{self.max_speed},Пробег:{self.mileage}')

bus = Autobus("Renault Logan", 180, 12)

bus.appellation()
    
