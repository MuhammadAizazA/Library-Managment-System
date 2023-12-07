import csv
import bookmodule
import re

pattern = r"(97[8|9]-\d{1,5}-\d{1,7}-\d{1,6}-\d)"

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


if __name__ == '__main__':
    """_summary_
    """
    # Generating a default admin
    file_path = 'Data/admins.csv'
    setup_admin(file_path)
    read_data = load_admin_into_objects(file_path)
    # Menu for showing Librarian Interface
    while (True):
        print(f'Hi {read_data.get_name()} You can perform the following operations')
        print('Press 1 to Add new Book to Library')
        print('Press 2 to Show all Books in Library')
        print('Press q to Exit')
        choice = input()
        if choice == '1':
            print('Enter Book Details')
            title = input('Enter the book Title: ')
            author = input('Enter the book Author: ')
            while True:
                isbn = input('Enter the book ISBN(13 digits): ')
                if len(isbn)==17:
                    if re.fullmatch(pattern, isbn):
                        print('Correct pattern')
                        break
                    else:
                        print('Incorrect pattern. Please enter a valid 13-digit ISBN.')


            num_of_copies = input('Enter the book Quantity: ')

            genre = int(input('Select the book Genre\n1: romance, 2: humour, 3: science fiction, 4: thriller, \n5: Biographies, 6: autobiographies, 7: memoirs'))
            genre_dict = {1: 'romance', 2: 'humour', 3: 'science fiction',4: 'thriller',
                          5: 'Biographies', 6: 'autobiographies', 7: 'memoirs\n: '}
            if genre >= 1 and genre <5:
                obj=bookmodule.FictionBook(title, author, isbn, num_of_copies, genre_dict[genre])
                obj.save_to_file()
            elif genre >= 5 and genre <=7:
                obj=bookmodule.NonFictionBook(title, author, isbn, num_of_copies, genre_dict[genre])
                obj.save_to_file()
        elif choice == '2':
            bookmodule.show_all_books()
        elif choice == 'q':
            exit()
