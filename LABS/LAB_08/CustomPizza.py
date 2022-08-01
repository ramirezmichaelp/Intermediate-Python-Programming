from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.strk=""
        
        if self.size=="S":
            self.price=8.00
        if self.size=="M":
            self.price=10.00
        if self.size=="L":
            self.price=12.00
            
    def addTopping(self,topping):
        if self.size=="S":
            extra=.50
        if self.size=="M":
            extra=0.75
        if self.size=="L":
            extra=1.00
        
        self.strk+="\t+ "+topping+"\n"
        self.price+=extra
        
            
            
    def getPizzaDetails(self): #stuck on this part

        strp=str(self.price)
        if strp.endswith(".0"):
            strp+="0"
        top=self.strk

        if top=="":
            s="CUSTOM PIZZA"+"\n"
            s+="Size: "+self.size+"\n"
            s+="Toppings:"+"\n"
            s+="Price: $"+strp
            s+="\n"
            return (s)
        else:
            s="CUSTOM PIZZA"+"\n"
            s+="Size: "+self.size+"\n"
            s+="Toppings:"+"\n"
            s+=top
            s+="Price: $"+strp
            s+="\n"
            return (s)        