from  src import bookmodule
import concurrent.futures

def show_all_books():
    """_summary_
    This function just read all the data by calling two functions and then print all the data
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        file_paths=['Data/fictionbooks.csv','Data/nonfictionbooks.csv']
        future = [executor.submit(bookmodule.load_books_into_list_objects, file_path) for file_path in file_paths]
    dict_list=[]
    
    for item in future:
            dict_list.append(item.result())
            
    
    objs_fic = bookmodule.create_books_objects(dict_list[0], bookmodule.FictionBook)
    objs_non_fic = bookmodule.create_books_objects(dict_list[1], bookmodule.NonFictionBook)    
    
    for dict_set in [objs_fic, objs_non_fic]:
        for book in dict_set:
            print(book)

if __name__=='__main__':      
    show_all_books()