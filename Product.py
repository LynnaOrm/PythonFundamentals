#Every method that doesnt have to return something should return self so methods can be chained.

class Product(object):

    def __init__(self,price,item,weight,brand,status):

        self.price = price
        self.item = item
        self.weight = weight
        self.brand = brand
        self.status = status


    def sell(self):
        self.status = sold
        return self


#tax as a decimal amount as a parameter and returns the price of the item including sales tax.
    def tax(self,tax):
        self.price = self.price * tax
        return self.price




#Method Return, takes reason for return as parameter and changes status accordingly. If item is being returned because it is defective change status to defective
#and change price to 0. If it is being returned in the box like new mark it for sale. if the box is open set status to used and apply 20% discount.

    def ReturnItem(self,reason):
        if self.reason == "defective":
            self.status = "defective"
            self.price = 0
        
        elif self.reason == "in the box, like new":
            self.status = "for sale!"
        
        elif self.reason == "box opened":
            self.status = "used"
            self.price -= self.price * .2
        return self




    def display_Info(self):
        print "Price: $", self.price
        print "Item: ", self.item
        print "Weight: ", self.weight, "lbs"
        print "Brand: ", self.brand
        print "Status: ", self.status
        print ""
        return self

Product1= Product(5000,"Lunar",5,"Nike","in the box, like new")



Product1.display_Info()