"""_summary_

    Returns:
        Main File : This File is the Library where Admin and Borrower can do the required Operations
        
"""
import logging
import adminmodule
import borrowermodule
import bookmodule
import re

pattern = r'(97[89]-\d{1,5}-\d{1,7}-\d{1,6}-\d{1})'

if __name__=='__main__':  
    while True:
        interface_choice=input('Continue as\nType LIB for Librarian\nType BRWR for Borrower\nType q to quit\n')
        if interface_choice=='LIB':
            # Generating a default admin
            file_path = 'Data/admins.csv'
            adminmodule.setup_admin(file_path)
            read_data = adminmodule.load_admin_into_objects(file_path)
            # Menu for showing Librarian Interface
            while (True):
                print(f'Hi {read_data.get_name()} You can perform the following operations')
                print('Press 1 to Add new Book to Library')
                print('Press 2 to Show all Books in Library')
                print('Press 3 to Show all borrowers in Library')
                print('Press 4 to Show average number Books borrowed')
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
                                print('Incorrect pattern. Please enter a valid (13 or 10 or 9)-digit ISBN.')
                        else:
                            print('Error: Lenght should be 13 with 4 (-) ie: 978-123-123-123-2')

                    num_of_copies = input('Enter the book Quantity: ')

                    genre = int(input('Select the book Genre\n1: romance, 2: humour, 3: science fiction, 4: thriller, \n5: Biographies, 6: autobiographies, 7: memoirs'))
                    genre_dict = {1: 'romance', 2: 'humour', 3: 'science fiction',4: 'thriller',
                                5: 'Biographies', 6: 'autobiographies', 7: 'memoirs\n'}
                    if genre >= 1 and genre <5:
                        obj=bookmodule.FictionBook(title, author, isbn, num_of_copies, genre_dict[genre])
                        obj.save_to_file()
                    elif genre >= 5 and genre <=7:
                        obj=bookmodule.NonFictionBook(title, author, isbn, num_of_copies, genre_dict[genre])
                        obj.save_to_file()
                elif choice == '2':
                    bookmodule.show_all_books()
                elif choice == '3':
                    borrowers_=borrowermodule.load_borrower_into_list_objects()
                    for _ in borrowers_:
                        print(_)
                elif choice == '4':
                    borrowers_=borrowermodule.load_borrower_into_list_objects()
                    adminmodule.show_averge_book_borrowed(borrowers_)
                elif choice == 'q':
                    break

        elif interface_choice=='BRWR':
            borrwoers_objects = borrowermodule.load_borrower_into_list_objects()
            path_fic = 'Data/fictionbooks.csv'
            path_nonfic = 'Data/nonfictionbooks.csv'
            fiction_dict = bookmodule.load_books_into_list_objects(path_fic)
            nonfiction_dict = bookmodule.load_books_into_list_objects(path_nonfic)
            fiction_objects = bookmodule.create_books_objects(
                fiction_dict, bookmodule.FictionBook)
            non_fiction_objects = bookmodule.create_books_objects(
                nonfiction_dict, bookmodule.NonFictionBook)

            logged_in_user = borrowermodule.login(borrwoers_objects)
            while True:
                print(
                    f'Hi {logged_in_user.get_name()} You can perform the following operations')
                print('Press 1 to borrow Book from Library')
                print('Press 2 to return book to Library')
                print('Press 3 to Show all Books in Library')
                print('Press 4 to Save all Books to file')
                print('Press q to Exit')
                browwer_choice = input('Your Choice: ')
                if browwer_choice == '1':
                    requested_isbn = input('Enter the ISBN you want to Borrow: ')
                    
                    for book_set in [fiction_objects, non_fiction_objects]:
                        for book in book_set:
                            if requested_isbn == book.get_isbn():
                                logged_in_user.borrow_book(requested_isbn, book_set)
                                break
                        else:
                            continue 
                        break
                    else:
                        print('Book not found. Please check the ISBN and try again.')
                elif browwer_choice == '2':
                    returned_isbn = input('Enter the ISBN you want to Return: ')
                    
                    for book_set in [fiction_objects, non_fiction_objects]:
                        for book in book_set:
                            if returned_isbn == book.get_isbn():
                                logged_in_user.return_book(returned_isbn, book_set)
                                break
                        else:
                            continue
                        break
                    else:
                        print('Book not found. Please check the ISBN and try again.')
                elif browwer_choice == '3':
                    bookmodule.show_all_books()
                elif browwer_choice == '4':
                    bookmodule.save_all_to_file(
                        fiction_objects, 'Data/fictionbooks.csv')
                    bookmodule.save_all_to_file(
                        non_fiction_objects, 'Data/nonfictionbooks.csv')
                    borrowermodule.save_borrowers_to_file(borrwoers_objects)
                elif browwer_choice == 'q':
                    break
        elif interface_choice=='q':
            print('Program Ended Successfully!')
            quit()