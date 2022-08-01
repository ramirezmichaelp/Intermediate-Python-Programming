
class Apartment:
    def __init__(self, rent=0, metersFromUCSB=0, condition="N/A"):
        self.rent=rent
        self.metersFromUCSB=metersFromUCSB
        self.condition=condition
        self.int=0
        if self.condition=="excellent":
            self.int=1
        if self.condition=="average":
            self.int=2
        if self.condition=="bad":
            self.int=3
        
    def getRent(self):
        return self.rent
    
    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    
    def getCondition(self):
        return self.condition
    
    def getApartmentDetails(self):
        T1=str(self.rent)
        T2=str(self.metersFromUCSB)
        T3=self.condition
        stR="(Apartment) Rent: $"+T1+", Distance From UCSB: "+T2+"m, Condition: "+T3
        return stR
    
    def __gt__(self, other):
        if self.rent> other.rent:
            return True
        if self.rent==other.rent and self.metersFromUCSB>other.metersFromUCSB:
            return True
        if self.rent==other.rent and self.metersFromUCSB==other.metersFromUCSB and self.int>other.int:
            return True
        
        return False
    
    def __eq__(self, other):
        if self.rent==other.rent and self.metersFromUCSB==other.metersFromUCSB and self.condition==other.condition:
            return True
        return False

    