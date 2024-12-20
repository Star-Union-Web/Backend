from library import Book
def to_dict_list(dict_list, books):
    dict_list = []
    for i in range(len(books)):
        dict_list.append(books[i].__dict__)
    return dict_list

def dict_list_to_obj(dict_list):
    objList = []
    for i in range(len(dict_list)):
        objList.append(Book(dict_list[i]["title"], dict_list[i]["author"], dict_list[i]["pub_year"], dict_list[i]["is_borrowed"]))
    return objList
