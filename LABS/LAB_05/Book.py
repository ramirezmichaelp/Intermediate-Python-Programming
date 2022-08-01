#michael P. Ramirez



class Book:
    def __init__(self, title="", author="", year=None):
        self.title=title
        self.author=author
        self.year=year
        
    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def getYear(self):
        return self.year
    
    
    def __gt__(self, other):
        if self.author>other.author:
            return True
        if self.author==other.author and self.year> other.year:
            return True
        if self.author==other.author and  self.year==other.year and self.title >other.title:
            return True
        return False
        
      
    def getBookDetails(self):
        t1=self.title
        t2=self.author
        t3=str(self.year)
        
        strR="Title: "+t1+", Author: "+t2+', Year: '+t3
        return strR