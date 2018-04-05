class book(object):
    #Define a book object
    def __init__(self, id, title, isbn, author, genre, publisher, summary):
        self.id = id
        self.title = title
        self.isbn = isbn
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.summary = summary