from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue

def test_pizza_price():
    a=Pizza("L")
    a.getPrice==0.0
    a.setPrice(100)
    a.getPrice=100

def test_pizza_size():
    a=Pizza("L")
    a.getSize()=="L"
    a.setSize("S")
    a.getSize=="S"

def test_custom_pizza_price():
    cp1 = CustomPizza("S")
    cp2 = CustomPizza("S")
    cp2.addTopping("extra cheese")
    assert cp1.getPrice()==8.00
    assert cp2.getPrice()==8.50


def test_custom_pizza_size():
    cp1 = CustomPizza("S")
    assert cp1.getSize()=="S"
    cp1.setSize("M")
    assert cp1.getSize()=="M"
    
def test_custom_pizza_str():
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n"


def test_special_pizza_price():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPrice()==12.00
        
def test_special_pizza_str():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
    
def test_P_Order_Time():
    cp1 = CustomPizza("S")
    order = PizzaOrder(123000)
    order.addPizza(cp1)
    assert order.getTime()==123000
    order.setTime(0)
    assert order.getTime()==0
    
def test_pizza_order_output():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)
    assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n" 
def test_heap_order():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order1=PizzaOrder(133050)
    order2=PizzaOrder(153555)
    order.addPizza(cp1)
    order.addPizza(sp1)
    order1.addPizza(cp1)
    order2.addPizza(sp1)
    x=OrderQueue()
    x.addOrder(order)
    x.addOrder(order1)
    x.addOrder(order2)
    assert x.processNextOrder()==\
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"