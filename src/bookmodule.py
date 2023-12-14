import csv
import concurrent.futures


def decorator(func):
    """_summary_

    Args:
        func (func): This is just decorator for Printing Books in Library
    """
    def wrapper(*arg, **kwarg):
        print('Name,Author,ISBN,Quantity,Genre')
        print('----------------------------------------------------')
        func(*arg, **kwarg)
        print('----------------------------------------------------')
    return wrapper


class Book:
    """
    This class is used to store book info
    """

    def __init__(self, title, auther, isbn, quantity_avalible):
        """_summary_
        this is called by both(FictionBook and NonFictionBook) inherited classes of book

        Args:
            title (str): to save book title
            auther (str): to save book auther
            isbn (str): _description_
            quantity_avalible (int): _description_
        """
        self.title = title
        self.auther = auther
        self.isbn = isbn
        self.quantity_avalible = int(quantity_avalible)

    def check_avalibility_book(self) -> bool:
        """_summary_
        this function checks if quantity of books are more then zero

        Returns:
            bool: this will return true if books are more then 0 or false if it's zero
        """
        if self.quantity_avalible > 0:
            return True
        else:
            return False

    def get_isbn(self):
        """_summary_

        Returns:
            _str_: _return isbn as string_
        """
        return self.isbn

    def get_quantity_avalible(self):
        """_summary_

        Returns:
            _int_: return quanity of books
        """
        return self.quantity_avalible

    def decrement_quantity(self):
        """_summary_
        This decrement value of books upon borrowing
        """
        self.quantity_avalible -= 1

    def increment_quantity(self):
        """_summary_
        This increment value of books upon returning
        """
        self.quantity_avalible += 1


class FictionBook(Book):
    """_summary_

    Args:
        Book (_FinctionBook_): _Just included genre in this inherited class_
    """

    def __init__(self, title, auther, isbn, quantity_avalible, genre):
        super().__init__(title, auther, isbn, quantity_avalible)
        self.genre = genre

    def __str__(self):
        return f'{self.title}, {self.auther}, {self.isbn}, {self.quantity_avalible}, {self.genre}'

    def save_to_file(self):
        data_to_append = {
            'title': self.title,
            'author': self.auther,
            'isbn': self.isbn,
            'quantity_available': self.quantity_avalible,
            'genre': self.genre
        }

        with open('Data/fictionbooks.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data_to_append.values())


class NonFictionBook(Book):
    """_summary_

    Args:
        Book (_FinctionBook_): _Just included genre in this inherited class_
    """

    def __init__(self, title, auther, isbn, quantity_avalible, genre):
        super().__init__(title, auther, isbn, quantity_avalible)
        self.genre = genre

    def __str__(self):
        return f'{self.title}, {self.auther}, {self.isbn}, {self.quantity_avalible}, {self.genre}'

    def save_to_file(self):
        data_to_append = {
            'title': self.title,
            'author': self.auther,
            'isbn': self.isbn,
            'quantity_available': self.quantity_avalible,
            'genre': self.genre
        }
        with open('Data/nonfictionbooks.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data_to_append.values())


def load_books_into_list_objects(file_path):
    """_summary_

    Args:
        file_path (_str_): the file is opened in read mode to fetch the data

    Returns:
        _dict_: _this will return all the data in dict form from csv file_
    """
    books_dictionary = {}
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, row in enumerate(csv_reader):
            books_dictionary[row[2]] = [row[0], row[1], row[3], row[4]]
    return books_dictionary


def create_books_objects(objs, booktype) -> list:
    """_summary_
    this function takes the dictionaies fetched from file in load_books_into_list_objects 
    function  and convert into the book inherited class type object and return it in list

    Args:
        objs (_type_): _description_
        booktype (_type_): _description_

    Returns:
        list: _description_
    """
    books_objects = []
    for index, (key, values) in enumerate(objs.items(), 0):
        new_borrower = f'borrower_{index}'
        books_objects.append(new_borrower)
        books_objects[index] = booktype(
            values[0], values[1], key, values[2], values[3])
    return books_objects


@decorator
def show_all_books():
    """_summary_
    This function just read all the data by calling two functions and then print all the data
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        file_paths=['Data/fictionbooks.csv','Data/nonfictionbooks.csv']
        future = [executor.submit(load_books_into_list_objects, file_path) for file_path in file_paths]
    dict_list=[]
    
    for item in future:
        dict_list.append(item.result())
            
    
    objs_fic = create_books_objects(dict_list[0], FictionBook)
    objs_non_fic = create_books_objects(dict_list[1], NonFictionBook)    
    
    for dict_set in [objs_fic, objs_non_fic]:
        for book in dict_set:
            print(book)


def save_all_to_file(books, file_path):
    """_summary_
    this function save the updated book objects in file in write mode 

    Args:
        books (_type_): _description_
        file_path (_type_): _description_
    """
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        unique_isbns = set()
        for book in books:
            if book.get_isbn() not in unique_isbns:
                data_to_append = {
                    'title': book.title,
                    'author': book.auther,
                    'isbn': book.isbn,
                    'quantity_available': book.quantity_avalible,
                    'genre': book.genre
                }
                writer.writerow(data_to_append.values())
                unique_isbns.add(book.isbn)

if __name__ == '__main__':
    # if this script is executed then all books in files will be displayed
    show_all_books()
