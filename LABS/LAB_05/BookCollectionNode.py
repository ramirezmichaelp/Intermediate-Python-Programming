#michael p ramirez



class BookCollectionNode:
    def __init__(self, data):
        self.next = None
        self.data = data
 

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext