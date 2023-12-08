import csv
import bookmodule
import re

class Librarian:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return (f'{self.name},{self.email},{self.password}')

    def get_name(self):
        return self.name

def load_admin_into_objects(file_path) -> Librarian:
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row1 = next(csv_reader)
        new_admin = Librarian(row1[0], row1[1], row1[2])
        return new_admin


def save_admins_into_file(file_path, data):
    try:
        with open(file_path, 'r') as file:
            is_empty = file.read(1) == ''
    except FileNotFoundError:
        is_empty = True

    with open(file_path, 'w', newline='') as file:
        fieldnames = ['name', 'email', 'password']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if is_empty:
            writer.writeheader()

        writer.writerows(data)


def setup_admin(file_path):
    admins_data = [
        {'name': 'admin',
         'email': 'admin',
         'password': 'admin'}
    ]
    save_admins_into_file(file_path, admins_data)

def show_averge_book_borrowed(borrwers):
    total_borrowed=0
    for bor in borrwers:
        total_borrowed+=bor.get_borrowed_books_number()
    
    print(f'Books Borrwed Average={total_borrowed//len(borrwers)}')

if __name__ == '__main__':
    """_summary_
    """
    # Generating a default admin
    file_path = 'Data/admins.csv'
    setup_admin(file_path)
    read_data = load_admin_into_objects(file_path)
    print(read_data)