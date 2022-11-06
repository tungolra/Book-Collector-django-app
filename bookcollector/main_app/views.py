from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import Book

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# def books_index(request):
#     books = Book.objects.all()
#     return render(request, 'books/index.html', {'books': books})


def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})


class BookCreate(generic.CreateView):
    model = Book
    # fields = ['author', 'title', 'genre', 'publish_year']
    fields = '__all__'
    success_url = '/books/'


class BookUpdate(generic.UpdateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'


class BookDelete(generic.DeleteView):
    model = Book
    success_url = '/books/'


# class HomeView(generic.View):
#     template_name = 'home.html'

# class AboutView(generic.View):
#     template_name = 'about.html'
# in a ListView, the queryset of model instances will be available via attributes named
# object_list and cat_list (again, the lowercase name of the Model with _list appended to it).
class IndexView(generic.ListView):
    model = Book
    template_name = 'books/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
#         # how to pass in booklist with CBV?

# class BookDetailsView(generic.DetailView):
#     model = Book
#     template_name = 'books/detail.html'
#     def get_queryset(self):
#         return super().get_queryset()
