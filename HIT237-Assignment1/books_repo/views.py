from django.shortcuts import render
from books_repo.book import book

# Create your views here.
def home(request):
    return render(request, 'base.html')

def books(request):
    page_data = {'book_list': get_books() }
    return render(request, 'books.html', page_data)

def datamodel(request):
    return render(request, 'datamodel.html')

def single_book(request, id):
    id = int(id)
    books = get_books()
    book = None
    for b in books:
        if b.id == id:
            book = b
    page_data = {'book': book }
    return render(request, 'book.html', page_data)

def get_books():
    booklist = []
    booklist.append(book(1,'Book1',15123123123,'Mr Author Page','space','Puffin','The book is about, etc'))
    booklist.append(book(2,'Book2',52342342349,'Mr Page File','space','Puffin','The book is about, etc'))
    return booklist