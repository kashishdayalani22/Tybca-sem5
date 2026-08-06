class Book:
    def __init__(self, pages):
        self.pages = pages

b1 = Book(92)
b2 = Book(183)
b3 = Book(151)
b4 = Book(264)

total_pages = b1.pages + b2.pages + b3.pages + b4.pages

print("Total number of pages in four books:", total_pages)
