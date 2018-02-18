#If the price is greater than 10,000 set the tax to be 15%, otherwise set the tax to be 12%.
#create 6 different instances of the class Car in the class have a method called display_all() that returns all the information about the car as a string. 


class Car(object):

    def __init__(self,price,speed,fuel,mileage):
        
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.price = price
    
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12

    
    def display_all(self):

        print "price: ", self.price

        print "speed: ", self.speed

        print "fuel: ", self.fuel

        print "mileage: ", self.mileage

        print "tax: ", self.tax


    

Honda = Car (2000,"35 mph","Full","15 mpg")
Lexus = Car (2000,"5 mph","Not Full","105 mpg")
Acura = Car (2000,"15 mph","Kind of Full","95 mpg")
Toyota = Car (2000,"25 mph","Full","25 mpg")
Ford = Car (2000,"45 mph","Empty","25 mpg")
Mercedes = Car (20000000,"35 mph","Empty","15mpg")



arrCar = [Honda, Lexus, Acura, Toyota, Ford, Mercedes]



for car in arrCar:

    car.display_all()
