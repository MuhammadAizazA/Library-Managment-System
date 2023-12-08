import csv

def decorator(func):
    def wrapper(*arg, **kwarg):
        print('----------------------------------------------------')
        func(*arg, **kwarg)
        print('----------------------------------------------------')
    return wrapper

class Book:
    def __init__(self, title, auther, isbn, quantity_avalible):
        self.title = title
        self.auther = auther
        self.isbn = isbn
        self.quantity_avalible = int(quantity_avalible)

    def check_avalibility_book(self) -> bool:
        if self.quantity_avalible > 0:
            return True
        else:
            return False

    def get_isbn(self):
        return self.isbn
    
    def get_quantity_avalible(self):
        return self.quantity_avalible
    
    def decrement_quantity(self):
        self.quantity_avalible-=1
    
    def increment_quantity(self):
        self.quantity_avalible+=1

class FictionBook(Book):
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
    books_dictionary = {}
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, row in enumerate(csv_reader):
            books_dictionary[row[2]] = [row[0], row[1], row[3], row[4]]
    return books_dictionary

def create_books_objects(objs,booktype) -> list:
    books_objects = []
    for index, (key, values) in enumerate(objs.items(), 0):
        new_borrower = f'borrower_{index}'
        books_objects.append(new_borrower)
        books_objects[index] = booktype(
            values[0], values[1],key, values[2], values[3])
    return books_objects

@decorator
def show_all_books():
    fic_objs = load_books_into_list_objects('Data/fictionbooks.csv')
    non_fic_objs = load_books_into_list_objects('Data/nonfictionbooks.csv')
    objs_fic = create_books_objects(fic_objs,FictionBook)
    objs_non_fic = create_books_objects(non_fic_objs,NonFictionBook)
    
    for _ in objs_fic:
        print(_)

    for _ in objs_non_fic:
        print(_)

def save_all_to_file(books, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            # Use a set to keep track of unique ISBNs
            unique_isbns = set()

            # Write data from all objects, avoiding duplicate ISBNs
            for book in books:
                if book.get_isbn() not in unique_isbns:
                    data_to_append = {
                        'title': book.title,
                        'author': book.auther,
                        'isbn': book.isbn,
                        'quantity_available': book.quantity_avalible,
                        'genre': book.genre  # Assuming genre is an attribute of some books
                    }
                    writer.writerow(data_to_append.values())
                    unique_isbns.add(book.isbn)

if __name__ == '__main__':
    show_all_books()
