from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
FORMATS = (
    ('S', 'Soft Cover'),
    ('H', 'Hard Cover'),
    ('E', 'Electronic Copy'),
    ('A', 'Audio Book')
)

class Subject(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'subject_id': self.id})


class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publish_year = models.IntegerField()
    subjects = models.ManyToManyField(Subject)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}: {self.title} ({self.publish_year})"

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'book_id': self.id})


class Format(models.Model):

    format = models.CharField(
        max_length=1,
        choices=FORMATS,
        default=FORMATS[0][0],
    )
    price = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Format: {self.get_format_display()}, Price: {self.price}"
