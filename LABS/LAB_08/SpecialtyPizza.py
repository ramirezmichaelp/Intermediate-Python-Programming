
from Pizza import Pizza

class  SpecialtyPizza(Pizza):
    def __init__(self, size, name=""):
        super().__init__(size)
        self.name=name
        if self.size=="S":
            self.price=12.00
        if self.size=="M":
            self.price=14.00
        if self.size=="L":
            self.price=16.00
        
    def getPizzaDetails(self): #stuck on this part
        s ="SPECIALTY PIZZA\n"
        s+="Size: "+self.size+"\n"
        s+="Name: "+self.name+'\n'
        s+="Price: $"+str(self.price)+"0\n"
        return (s)