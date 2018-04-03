from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def books(request):
    page_data = {'book_list': get_books() }
    return render(request, 'books.html', page_data)

def single_book(request, id):
    id = int(id)
    books = get_books()
    book = None
    for b in books:
        if b.id == id:
            book = b
    page_data = {'book': book }
    return render(request, 'book.html', page_data)

class Book:
    def __init__(self, id, title, isbn, author, genre, publisher, summary):
        self.id = id
        self.title = title
        self.isbn = isbn
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.summary = summary

def get_books():
    booklist = []
    booklist.append(Book(1,'Book1',15123123123,'Mr Author Page','space','Puffin','The book is about, etc'))
    booklist.append(Book(2,'Book2',52342342349,'Mr Page File','space','Puffin','The book is about, etc'))
    return booklist