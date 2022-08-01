from Apartment import Apartment
from lab06 import mergesort
from lab06 import ensureSortedAscending
from lab06 import getNthApartment
from lab06 import getTopThreeApartments
def test_getRent():
    a0 = Apartment(1204, 200, "bad")
    assert a0.getRent()==1204
    a1=Apartment()
    assert a1.getRent()==0
    
def test_getMeters():
    a0 = Apartment(1204, 200, "bad")
    assert a0.getMetersFromUCSB()==200
    a1=Apartment()
    assert a1.getMetersFromUCSB()==0

def test_get_condition():
    a0 = Apartment(1204, 200, "bad")
    assert a0.getCondition()=="bad"
    a1 = Apartment()
    assert a1.getCondition()=="N/A"
    
def test_get_details():
    x='(Apartment) Rent: $1204, Distance From UCSB: 200m, Condition: bad'
    a0 = Apartment(1204, 200, "bad")
    assert a0.getApartmentDetails()==x

   

    
def test_n_apartmetn():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    unsora0="(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"
    unsoran="(Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent"
    sorta0="(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    sortan="(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"
    length = len(apartmentList)
    assert getNthApartment(apartmentList, 0)==unsora0
    assert getNthApartment(apartmentList, length-1)==unsoran
    mergesort(apartmentList)
    assert getNthApartment(apartmentList, 0)==sorta0
    assert getNthApartment(apartmentList, length-1)==sortan

def test_top():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    str1="1st: (Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    str2="2nd: (Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent"
    str3='3rd: (Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: average'
    strR=str1+"\n"+str2+"\n"+str3
    strR2=str1+"\n"+str2

    apartmentList = [a0, a1, a2, a3, a4, a5]
    List2=[a4,a5]
    assert getTopThreeApartments(apartmentList)==strR
    assert getTopThreeApartments(List2)==strR2

    
def test_order():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    Alist=[a4,a5,a2,a1,a0,a3]
    ensureSortedAscending(Alist)==True
    Blist=[a4,a5,a2,a1,a3,a0]
    ensureSortedAscending(Blist)==False
    
def test_eq():
    a0 = Apartment(1200, 200, "average")
    a10 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a6 = Apartment(1200, 210, "average")
    assert (a0==a1)==False
    assert (a0==a6)==False
    assert (a0==a10)==True
    
def test_gt():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a5 = Apartment(800, 250, "excellent")
    assert(a0>a1)==True
    assert(a1>a0)==False
    assert(a0>a5)==True
    