from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def books(request):
    page_data = {'book_list': get_books() }
    return render(request, 'books.html', page_data)

class Book:
    def __init__(self, id, title, isbn, author):
        self.id = id
        self.title = title
        self.isbn = isbn
        self.author = author

def get_books():
    booklist = []
    booklist.append(Book(1,'Book1','15123123123','Mr Author Page'))
    booklist.append(Book(2,'Book2','52342342349','Mr Page File'))
    return booklist