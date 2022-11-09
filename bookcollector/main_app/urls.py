from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('books/', views.IndexView.as_view(), name='books_index'),
    path('books/', views.books_index, name='books_index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('books/create/', views.BookCreate.as_view(), name="books_create"),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
    path('books/<int:book_id>/add_format/',
         views.add_format, name='add_format'),
    path('books/<int:book_id>/assoc_subject/<int:subject_id>/',
         views.assoc_subject, name='assoc_subject'),
    path('books/<int:book_id>/unassoc_subject/<int:subject_id>/',
         views.unassoc_subject, name='unassoc_subject'),
    path('accounts/signup/', views.signup, name='signup')
    # path('subjects/', views.SubjectList.as_view(), name='subjects_index')
]
