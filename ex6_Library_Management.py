class library:
    
    library_nos = 0  # this gets treatded as static variable and is attached to the class static variable are intilalized only once 
    
    def __init__(self):

        library.library_nos += 1
        self.books = []  ## these are the isntance variable or what you call attributes of object
        self.no_of_books = 0 
    
    def printall_books(self):
        print(self.books)
    
    def add_book(self,book_name):
        self.books.append(book_name)
        self.no_of_books = len(self.books)


    def get_number_of_books(self):
        print("The Number of Book does not Match List Length") if(self.no_of_books != len(self.books)) else print(f"The number of books are {self.no_of_books}")


obj1 = library()
obj1.add_book("war and peace")
obj1.add_book("intellignet investor")
obj1.add_book("psychology of money")
obj1.get_number_of_books()

#showing the use of static variable
print(library.library_nos)

