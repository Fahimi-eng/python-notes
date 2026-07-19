class Library:
    __books =  []

    def __init__(self):
        pass

    if __name__  == "__main__":
        pass
    
    def add_book(self,title, author):
        self.__books.append({'title': title, 'author': author})
        return True
    
    def remove_book(self, title):
        for  book in self.__books:
            if book['title']  == title:
                self.__books.remove(book)   
                return True
        return False     

    def search_book(self, title):
        for  book in self.__books:
            if book['title']  == title: 
                return book
        return False   

    def show_books(self):
        return self.__books
    

if __name__  == "__main__":
    import subprocess
    import os

    def clear():
        subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)

    def showMenu():
        print('------------> Welcome To Book Shop <------------ \n')
        print('1_ Show All Books in Shop.')
        print('2_ Search a Book.')
        print('3_ Add a Book.')
        print('4_ Remove a Book.\n')
        print('0_ Exit.\n')
    
    lib_obj = Library()
    exit = False
    while(not exit):
        showMenu()
        switch = int(input('Enter a Number to Continue: '))

        if 0 < switch < 5:
            if switch == 1:
                print('************************************')
                print(lib_obj.show_books())
                print('************************************')
            elif switch ==2:
                book_name = input('Enter Book Title to Search: ')
                if lib_obj.search_book(book_name) == False:
                    print('************************************')
                    print('******** There is no Book **********')
                    print('************************************')
                    print()
                else:
                    print('************************************')
                    print(lib_obj.search_book(book_name))
                    print('************************************')
                    print()
                    
            elif switch ==3:
                title = input('Enter Book Title: ')
                author = input("Enter Book Author:  ")
                if lib_obj.add_book(title, author):
                    print()
                    print('************************************')
                    print("**** Your Book Added to Library ****")
                    print('************************************')
                    print()


            else:
                title = input('Enter Book Title to Remove: ')
                if lib_obj.remove_book(title):
                    print('************************************')
                    print('******** Book Removed. *************')
                    print('************************************')
                    print()

                else:
                    print('************************************')
                    print('** There is no Book by This Title **')
                    print('************************************')
                    print()

        elif switch == 0:
            exit = True
        else:
            clear()
