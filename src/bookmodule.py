import csv

def decorator(func):
    def wrapper(*arg, **kwarg):
        print('----------------------------------------------------')
        func(*arg, **kwarg)
        print('----------------------------------------------------')
    return wrapper

class Book:
    quantity_avalible:int
    def __init__(self, title, auther, isbn, quantity_avalible):
        self.title = title
        self.auther = auther
        self.isbn = isbn
        self.quantity_avalible = int(quantity_avalible)

    def check_avalibility_book(self) -> bool:
        if self.quantity_available > 0:
            return True
        else:
            return False

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
            key, values[0], values[1], values[2], values[3])
    return books_objects


@decorator
def show_all_books():
    fic_objs = load_books_into_list_objects('Data/fictionbooks.csv')
    non_fic_objs = load_books_into_list_objects('Data/nonfictionbooks.csv')
    objs_fic = create_books_objects(fic_objs,FictionBook)
    for _ in objs_fic:
        print(_)

    objs_non_fic = create_books_objects(non_fic_objs,NonFictionBook)
    for _ in objs_non_fic:
        print(_)


if __name__ == '__main__':
   
    non_fiction_book_1 = NonFictionBook('zzzz1', 'zzzzz', '1343421', 10, 'Sci-fi')
    non_fiction_book_2 = NonFictionBook('zzzz2', 'zzzzz', '1343422', 10, 'Sci-fi')
    non_fiction_book_3 = NonFictionBook('zzzz3', 'zzzzz', '1343423', 10, 'Sci-fi')
    non_fiction_book_4 = NonFictionBook('zzzz4', 'zzzzz', '1343424', 10, 'Sci-fi')
    fiction_book_1 = FictionBook('aaaaa1', 'aaaa', '234434212', 10, 'Sci-fi')
    fiction_book_2 = FictionBook('aaaaa2', 'aaaa', '234434214', 10, 'Sci-fi')
    fiction_book_3 = FictionBook('aaaaa3', 'aaaa', '234434216', 10, 'Sci-fi')
    fiction_book_4 = FictionBook('aaaaa4', 'aaaa', '234434218', 10, 'Sci-fi')
    non_fiction_book_1.save_to_file()
    non_fiction_book_2.save_to_file()
    non_fiction_book_3.save_to_file()
    non_fiction_book_4.save_to_file()
    fiction_book_1.save_to_file()
    fiction_book_2.save_to_file()
    fiction_book_3.save_to_file()
    fiction_book_4.save_to_file()
    show_all_books()
