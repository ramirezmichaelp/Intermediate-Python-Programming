from Pizza import Pizza
from CustomPizza import Pizza
from SpecialtyPizza import SpecialtyPizza
class PizzaOrder():
    def __init__(self,time=0):
        self.pizzas=[]
        self.time=time
        self.total=0
        self.string=""
        

        
    def getTime(self):
        return self.time
    
    def setTime(self,time):
        self.time=time
        
        
    def addPizza(self,pizza):
        self.pizzas.append(pizza)
        self.total+=pizza.getPrice()
        self.string+=pizza.getPizzaDetails()+"\n----\n"
        
    def getOrderDescription(self):
        s=""
        strp=str(self.total)
        if strp.endswith(".0"):
            strp+="0"
        s_intro="******\n"
        time="Order Time: "+str(self.time)+"\n"
        body=self.string
        
        if len(self.pizzas)==0:
            s+=s_intro
            s+=time
            s+="TOTAL ORDER PRICE: $0.00"
            s+=s_intro
            return(s)
            
        else:
            s+=s_intro
            s+=time
            s+=body
            s+='TOTAL ORDER PRICE: $'+strp+'\n'
            s+=s_intro
            return (s)