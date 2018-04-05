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
    booklist.append(book(1,'Kill Shot',9780857208675,'Vince Flynn','Thriller','Simon & Schuster','For months, Mitch Rapp has been steadily working his way through a list of the men responsible for the slaughter of 270 civilians including his own girlfriend in the Pan Am Lockerbie bombing. His next target is a Libyan diplomat.'))
    booklist.append(book(2,'American Assassin',9781847398055,'Vince Flynn','Thriller','Simon & Schuster','Before he was considered a CIA-super agent, before he was thought of as a terrorist\'s worst nightmare, and before he was both loathed and admired by politicians on Capitol Hill, Mitch Rapp was a star college athlete with an untapped instinct for violence.'))
    booklist.append(book(3,'Consent to Kill',9781847395719,'Vince Flynn','Thriller','Simon & Schuster','For more than ten years, Mitch Rapp has been on the frontline of the War against Terror. His bold actions have saved the lives of thousands - but in the process his list of enemies has grown inexorably.'))
    booklist.append(book(4,'Ice Station',9781742611747,'Matthew Reilly','‎Techno-thriller','Pan Macmillan Australia','At a remote ice station in Antarctica, a team of US scientists has found something buried deep within a 100-million-year-old layer of ice. Something made of metal.'))
    booklist.append(book(5,'Seven Ancient Wonders',9781742611730,'Matthew Reilly','Thriller','Pan Macmillan Australia','Two thousand years ago, it was hidden within the Seven Wonders of the Ancient World. Now, in the present day, it must be found again... Captain Jack West Jr - part soldier, part scholar, all hero.'))
    booklist.append(book(6,'Nineteen Eighty-Four',9781784043735,'George Orwell','Political Fiction','Arcturus Publishing','George Orwell\'s dystopian masterpiece, Nineteen Eighty-Four is perhaps the most pervasively influential book of the twentieth century, making famous Big Brother, newspeak and Room 101.\'Who controls the past controls the future: who controls the present controls the past\''))
    booklist.append(book(7,'Dune',9780881036367,'Frank Herbert','Science Fiction','Ace Books','This Hugo and Nebula Award winner tells the sweeping tale of a desert planet called Arrakis, the focus of an intricate power struggle in a byzantine interstellar empire.'))
    return booklist