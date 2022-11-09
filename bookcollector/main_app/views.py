from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book, Format, Subject, User
from .forms import FormatForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# class IndexView(generic.ListView):
#     model = Book
#     template_name = 'books/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
@login_required
def books_index(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'books/index.html', {'books': books})


@login_required
def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    subjects_book_doesnt_have = Subject.objects.exclude(
        id__in=book.subjects.all().values_list('id'))
    format_form = FormatForm()
    return render(request, 'books/detail.html', {
        'book': book, 'format_form': format_form, 'exclSubjects': subjects_book_doesnt_have
    })


class BookCreate(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['author', 'title', 'genre', 'publish_year']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    # success_url = '/books/'


class BookUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = '__all__'


class BookDelete(LoginRequiredMixin, generic.DeleteView):
    model = Book
    success_url = '/books/'


def add_format(request, book_id):
    form = FormatForm(request.POST)
    if form.is_valid():
        new_format = form.save(commit=False)
        new_format.book_id = book_id
        new_format.save()
    return redirect('books:detail', book_id)


# class SubjectList(generic.ListView):
#     model = Subject
@login_required
def assoc_subject(request, book_id, subject_id):
    Book.objects.get(id=book_id).subjects.add(subject_id)
    return redirect('books:detail', book_id)


@login_required
def unassoc_subject(request, book_id, subject_id):
    Book.objects.get(id=book_id).subjects.remove(subject_id)
    return redirect('books:detail', book_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books:books_index')
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
