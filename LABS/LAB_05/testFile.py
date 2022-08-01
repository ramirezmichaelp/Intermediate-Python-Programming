from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection

def test_getTitle():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getTitle()=="Ready Player One"
    a=Book("Big Red","George Martin",1977)
    assert a.getTitle()=="Big Red"
    c=Book()
    assert c.getTitle()==''

    
def test_getAuthor():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getAuthor()=="Cline, Ernest"
    a=Book("Big Red","George Martin",1977)
    assert a.getAuthor()=="George Martin"
    c=Book()
    assert c.getAuthor()==""
    
def test_getYear():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getYear()==2011
    a=Book("Big Red","George Martin",1977)
    assert a.getYear()==1977
    c=Book()
    assert c.getYear()==None

def test_getInfo():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getBookDetails()== 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011'
    b3 = Book("Rage", "King, Stephen", 1977)
    assert b3.getBookDetails()=="Title: Rage, Author: King, Stephen, Year: 1977"

def test_emptyBooksCollection():
    book1 = BookCollection()
    assert book1.isEmpty()==True
    b0 = Book("Cujo", "King, Stephen", 1981)
    bc = BookCollection()
    bc.insertBook(b0)
    assert bc.isEmpty()==False
    
def test_getnumberofBooks():
    book1 = BookCollection()
    assert book1.getNumberOfBooks()==0
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getNumberOfBooks()==3
    
   
def test_getbyAuthor():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The fox", "Big Bob", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    assert bc.getBooksByAuthor("KING, Stephen")=="Title: Cujo, Author: King, Stephen, Year: 1981"+"\n"
    
def test_getAll():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    b2a=b2.getBookDetails()
    b3a=b3.getBookDetails()
    b1a=b1.getBookDetails()
    b0a=b0.getBookDetails()

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    xxx=b2a+"\n"+b3a+"\n"+b1a+"\n"+b0a+"\n"
    assert bc.getAllBooksInCollection()==xxx
    

    
    
    