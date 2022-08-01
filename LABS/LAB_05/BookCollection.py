#Michael Ramirez

from Book import Book
from BookCollectionNode import BookCollectionNode


class BookCollection:
    def __init__(self):
        self.head = None
        self.size=0
    
    def isEmpty(self):
        return self.head==None
    
    def getNumberOfBooks(self):
        return self.size

    def insertBook(self, book):
        self.size+=1
        current = self.head
        previous = None
        stop = False
        
        while current != None and not stop:
            if current.getData() > book:
                stop = True
                
            else:
                previous = current
                current = current.getNext()

        temp =BookCollectionNode(book)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

        



    def getBooksByAuthor(self, author):
        # initialize current node to head
        current= self.head

        output=""

        while current !=None:
            if current.getData().getAuthor().upper() == author.upper():
                output+=(current.getData().getBookDetails())+"\n"
            current=current.getNext()

       
        #output = output[:len(output)-1]
        return output

    def getAllBooksInCollection(self):
        current=self.head
        output=""
        while current !=None:
            output += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        #output = output[:len(output)-1]
        return output
            

       

       