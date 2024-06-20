# CREATE A CLASS CALLED CARS WITH THE FOLLOWING ATTRIBUTES
# MODEL, YEAR OF MANUFACTURE,TYPE,COLOR

# CREATE A METHOD TO PRINT
# "MY DREAM CAR IS.... MANUFACTURES IN....BEING A.... TYPE,.... IN COLOR"

# INITIALIZE WITH AT LEAST 5 OBJECTS

class Cars:
    def __init__(self, model, yearofmanufacture, type, color):
        self.model = model
        self.yearofmanufacture = yearofmanufacture
        self.type = type
        self.color = color

    def display(self):
        print(self.model, self.yearofmanufacture, self.type, self.color)


my_cars = Cars(model='BMW', yearofmanufacture='1928', type='M8. Convertible', color='black')
my_cars.display()
my_cars2 = Cars(model='Ferrari', yearofmanufacture='1939', type='LaFerrari', color='blue')
my_cars2.display()
my_cars3 = Cars(model='Bugatti', yearofmanufacture='1909', type='Bugatti Chiro', color='red')
my_cars3.display()
my_cars4 = Cars(model='Mercedes', yearofmanufacture='1926', type='cabriolet', color='maroon')
my_cars4.display()
my_cars5 = Cars(model='Chevrolet', yearofmanufacture='1913', type='SUV', color='white')
my_cars5.display()
