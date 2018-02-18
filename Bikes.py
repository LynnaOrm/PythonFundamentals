class Bike(object):

    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
        



    def displayInfo(self):
        print 'Price: $' + str(self.price) 
        print 'Max Speed:' +str(self.max_speed) + 'mph'
        print 'Total Miles:' +str(self.miles) +'miles'
       


    def ride(self):
        print "Riding..."
        self.miles =+ 10


    def reverse(self):

        if self.miles >=5:
            self.miles -= 5
        print "Reversing..."



bike1 = Bike(50,32)
bike2 = Bike(250,51)
bike3 = Bike(10,6)



bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()



bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()



bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()