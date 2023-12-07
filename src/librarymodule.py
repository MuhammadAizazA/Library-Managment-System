import adminmodule
import borrowermodule
import bookmodule
import re

pattern = r"(97[8|9]-\d{1,5}-\d{1,7}-\d{1,6}-\d)"

# def average_books_borrowed(*arg):
#     for book in arg:
#         book.

if __name__=='__main__':
    while True:
        interface_choice=input('Continue as\nType ADM for Librarian\nType BRWR for Borrower\n')
        if interface_choice=='adm':
            # Generating a default admin
            file_path = 'Data/admins.csv'
            adminmodule.setup_admin(file_path)
            read_data = adminmodule.load_admin_into_objects(file_path)
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
        
        
                borrowers_=borrowermodule.load_borrower_into_list_objects()
        
                print(borrowers_[0])
        elif interface_choice=='BRWR':
            print('Nothing')