import csv
import os
import logging.config

import yaml

def setup_logging(default_path='logs/logging.yaml',default_level=logging.INFO,env_key='LOG_CFG'):
    """Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

class Borrower:
    def __init__(self, name, address, email, password, borrowed_books_number, borrowed_isbns):
        self.name = name
        self.address = address
        self.borrowed_books_number = int(borrowed_books_number)
        self.email = email
        self.password = password
        self.borrowed_isbns = list(borrowed_isbns.split(' '))

    def get_borrowed_books_number(self):
        return self.borrowed_books_number
    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_borrowed_isbns(self):
        return self.borrowed_isbns

    def add_borrowed_isbns(self, new_isbn):
        self.borrowed_isbns.append(new_isbn)

    def add_borrowed_isbns(self, returned_isbn):
        try:
            self.borrowed_isbns.remove(returned_isbn)
        except Exception as e:
            print(f"{returned_isbn} not found in the list.", e)

    def increment_borrowed_books_number(self):
        self.borrowed_books_number += 1

    def decrement_borrowed_books_number(self):
        self.borrowed_books_number -= 1

    def __str__(self):
        return (f'{self.name},{self.email},{self.password},{self.address},{self.borrowed_books_number},{self.borrowed_isbns}')

    def borrow_book(self, applied_isbn, books):
        for book in books:
            if applied_isbn == book.get_isbn():
                try:
                    if book.check_avalibility_book():
                        setup_logging()
                        book.decrement_quantity()
                        self.increment_borrowed_books_number()
                        self.borrowed_isbns.append(book.get_isbn())
                        print(self.borrowed_isbns)
                        logging.info(f'Book ISBN: {applied_isbn} Borrowed Successfully')
                except Exception as e:
                    print('Book Out of Stock!', e)

    def return_book(self, returned_isbn, books):
        for book in books:
            if returned_isbn == book.get_isbn():
                try:
                    # Check if the borrower has borrowed this book
                    if returned_isbn in self.borrowed_isbns:
                        setup_logging()
                        book.increment_quantity()
                        self.decrement_borrowed_books_number()
                        self.borrowed_isbns.remove(returned_isbn)
                        print(f'Returned book with ISBN {returned_isbn}')
                        print(f'Updated borrowed ISBNs: {self.borrowed_isbns}')
                        logging.info(f'Book ISBN: {returned_isbn} Returned Successfully')
                    else:
                        print('You have not borrowed this book.')
                except Exception as e:
                    print(f'Error returning book: {e}')

def load_borrower_into_list_objects() -> list:
    borrower_dictionary = {}
    borrower_objects = []
    with open('Data/borrower.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, row in enumerate(csv_reader):
            borrower_dictionary[row[0]] = [
                row[1], row[2], row[3], row[4], row[5]]

    for index, (key, values) in enumerate(borrower_dictionary.items(), 0):
        new_borrower = f'borrower_{index}'
        borrower_objects.append(new_borrower)
        borrower_objects[index] = Borrower(
            key, values[0], values[1], values[2], values[3], values[4])

    return borrower_objects

def login(borrowers_objects):
    while True:
        try:
            email = input('Enter Your Email: ')
            password = input('Enter Your Password: ')

            for borrower in borrowers_objects:
                if borrower.get_email() == email and borrower.get_password() == password:
                    print(f'Login successful for {borrower.get_name()}')
                    return borrower

        except StopIteration:
            print('Invalid email or password. Please try again.')


def save_borrowers_to_file(borrower_objects):
    with open('Data/borrower.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for borrower in borrower_objects:
            borrowed_isbns=' '.join(borrower.borrowed_isbns)
            writer.writerow([borrower.name, borrower.address, borrower.email, borrower.password,
                            borrower.borrowed_books_number, borrowed_isbns])

if __name__ == '__main__':
    borrwoers_objects = load_borrower_into_list_objects()
    for _ in borrwoers_objects:
        print(_)
