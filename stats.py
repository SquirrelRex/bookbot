def sort_on(items):
    return items["num"]

def get_book_text(book_path):
    with open(book_path) as f:
        text_as_string = f.read()
    return text_as_string

def get_num_words(book_path):
    book = get_book_text(book_path)
    words = book.split()
    return len(words)

def get_num_charactors(book_path):
    book = get_book_text(book_path)
    book = book.lower()
    num_charactors = {}
    for letter in book:
        if letter.isalpha():
            if letter in num_charactors:
                num_charactors[letter] += 1
            else:
                num_charactors[letter] = 1
    return num_charactors

def sort_chars(book):
    chars_dict = get_num_charactors(book)
    chars_list = [{"char": k, "num": v} for k,v in chars_dict.items()]
    chars_list.sort(reverse=True,key=sort_on)
    return(chars_list)