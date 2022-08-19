# encapsulation using get and set method
class Library:
    def __init__(self, id, name):
        self.bookId = id
        self.bookName = name

    def setBookName(self, newBookName):
        self.bookName = newBookName

    def getBookName(self):
        print(f"The name of book is {self.bookName}")


book = Library(101, "The Witchers")
book.getBookName()
book.setBookName("The Witchers Returns")
book.getBookName()
