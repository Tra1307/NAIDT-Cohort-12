class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.__model = model
        self.year = year
        self.color = color

    def get_model(self):
        return self.__model

    def drive(self):
        print('This '+self.model+' is driving')

    def stop(self):
        print('This '+self.model+' is stropped')
        

car_1 = Car('Chevy', 'Corvette',2012,'Blue')
car_1.drive()



    
