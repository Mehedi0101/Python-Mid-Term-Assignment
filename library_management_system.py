class Library:
    book_list = []

    @classmethod
    def entry_book(self,book_id,title,author,availability):
        self.book_list.append(Book(book_id,title,author,availability))

class Book(Library):
    def __init__(self,book_id,title,author,availability):
        super().__init__()
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

    @classmethod
    def borrow_book(self,id):
        pos = -1
        for idx,book in enumerate(self.book_list):
            if book.__book_id == id:
                pos = idx
        
        if pos != -1:
            if self.book_list[pos].__availability:
                self.book_list[pos].__availability = False
                print(f'"{self.book_list[pos].__title}" has been issued to you')
            else:
                print(f'"{self.book_list[pos].__title}" is currently not available')
        else:
            print(f'Please enter a valid book id')
    
    @classmethod
    def return_book(self,id):
        pos = -1
        for idx,book in enumerate(self.book_list):
            if book.__book_id == id:
                pos = idx
        
        if pos != -1:
            if self.book_list[pos].__availability == False:
                self.book_list[pos].__availability = True
                print(f'You have successfully returned "{self.book_list[pos].__title}". Thank you!')
            else:
                print(f'Please enter the correct book id')
        else:
            print(f'Please enter a valid book id')
    
    @classmethod
    def view_book_info(self):
        print('\n')
        for book in self.book_list:
            print(f'id: {book.__book_id}, title: {book.__title}, author: {book.__author}, available: {book.__availability}')


Library.entry_book(1001, "Sherlock Holmes", "Sir Arthur Conan Doyle", True)
Library.entry_book(1002, "Harry Potter and The Chamber of Secrets", "JK Rowling", True)
Library.entry_book(1003, "Professor Shonku", "Satyajit Ray", True)
Library.entry_book(1004, "Misir Ali", "Humayun Ahmed", True)
Library.entry_book(1005, "The Hobbit", "J.R.R. Tolkien", True)
Library.entry_book(1006, "The Witcher: Sword of Destiny", "Andrzej Sapkowski", True)
Library.entry_book(1007, "A Song of Ice and Fire", "George R. R. Martin", True)
Library.entry_book(1008, "The Chornicles of Narnia", "C. S. Lewis", True)
Library.entry_book(1009, "Crime and Punishment", "Fyodor Dostoevsky", True)
Library.entry_book(1010, "Jane Eyre", "Charlotte Brontë", True)


print('---------- Library Management System ----------\n')

def show_options():
    print('\nList of options')
    print('-----------------')
    print('1. View All Books')
    print('2. Borrow Book')
    print('3. Return Book')
    print('4. Exit')

def select_option():
    x = int(input('\nEnter an option: '))
    return x

while True:
    show_options()
    op = select_option()
    if op == 1:
        Book.view_book_info()
    elif op == 2:
        id = int(input('Enter the book id that you want to borrow: '))
        Book.borrow_book(id)
    elif op == 3:
        id = int(input('Enter the book id that you want to return: '))
        Book.return_book(id)
    elif op == 4:
        break
    else:
        print('Please enter a valid option')