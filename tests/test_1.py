import re

pattern = r"(97[8|9]-\d{1,5}-\d{1,7}-\d{1,6}-\d)"

if __name__ == "__main__":
    while True:
        isbn = input('Enter the book ISBN(13 digits): ')
        if len(isbn)==17:
            if re.fullmatch(pattern, isbn):
                print('Correct pattern')
                break
            else:
                print('Incorrect pattern. Please enter a valid 13-digit ISBN.')
            
        

            
