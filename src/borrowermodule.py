import csv
import bookmodule

class Borrower:
    borrowed_isbns:list
    borrowed_books_number:int
    def __init__(self,name,address,email,borrowed_books_number,password,borrowed_isbns):
        self.name=name
        self.address=address
        self.borrowed_books_number=int(borrowed_books_number)
        self.email=email
        self.password=password
        self.borrowed_isbns=list(borrowed_isbns.split(' '))

    def __str__(self):
        return (f'{self.name},{self.email},{self.password},{self.address},{self.borrowed_books_number},{self.borrowed_isbns}')
    
    # def borrow_book(self,applied_isbn,books:Books):
    #    if applied_isbn
    #       print(" ".join(values[4]))
    
    # def return_book():
    #     pass

def load_borrower_into_list_objects()->list:
    borrower_dictionary={}
    borrower_objects=[]
    with open('Data/borrower.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for index,row in enumerate(csv_reader):
            borrower_dictionary[row[0]]=[row[1],row[2],row[4],row[5],row[5]]
       
    for index, (key, values) in enumerate(borrower_dictionary.items(), 0):
        new_borrower = f'borrower_{index}'
        borrower_objects.append(new_borrower)
        borrower_objects[index]=Borrower(key,values[0],values[1],values[2],values[3],values[4])

    return borrower_objects

# def average_book_borrowed():
    
if __name__=='__main__':
    borrwoers_objects=load_borrower_into_list_objects()
    path_fic='Data/fictionbooks.csv'
    path_nonfic='Data/nonfictionbooks.csv'
    fiction_dict=bookmodule.load_books_into_list_objects(path_fic)
    nonfiction_dict=bookmodule.load_books_into_list_objects(path_nonfic)
    fiction_objects=bookmodule.create_books_objects(fiction_dict,bookmodule.FictionBook)
    non_fiction_objects=bookmodule.create_books_objects(nonfiction_dict,bookmodule.NonFictionBook)
    
    fiction_objects
    print(len(borrwoers_objects))
    for borrwoer_ in borrwoers_objects:
        print(borrwoer_.borrowed_books_number)
    
    for fiction_book in fiction_objects:
        print(fiction_book.quantity_avalible)
    for non_fiction_book in non_fiction_objects:
        print(non_fiction_book.quantity_avalible)
