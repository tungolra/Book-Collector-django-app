from django.shortcuts import render
from django.http import HttpResponse

# temporary place for Books model 
class Book: 
    def __init__(self, author, title, genre, publish_date): 
        self.author = author
        self.title = title
        self.genre = genre
        self.publish_date = publish_date

books = [
    Book("Barbara Oakley", "A Mind for Numbers - How to Excel at Math and Science (Even If You Flunked Algebra)", "Math", 2014), 
    Book("Steven C. Hayes", "A Liberated Mind - How to Pivot Toward What Matters", "Self-Help", 2019),
    Book("Daniel Kahneman", "Thinking Fast and Slow", "Popular Science", 2011)
]
# Create your views here.
def home(request): 
    return HttpResponse("Hello")

def about(request): 
    return render(request, 'about.html')

def books_index(request): 
    return render(request, 'books/index.html', {'books': books})