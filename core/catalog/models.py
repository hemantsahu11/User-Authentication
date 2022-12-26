from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)   # if by mistake the author is deleted then set this to null on_delete
    summary = models.TextField(max_length=200)
    isbn = models.CharField('ISBN', max_length=13,unique=True)
    genre = models.ManyToManyField(Genre)   # by using this statement we are maintaining many to many relationships between genre
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)  # getting error if true is not null
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    #.....


class Author(models.Model):
    name = models.CharField(max_length=60)
    date_of_birth = models.DateField(null=True, blank=True)

    # class Meta:
    #     ordering = ['first name' , 'last name' ]   # use this when we have to change the order in db

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


import uuid  # for generating unique ids
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT)   # this will restrict the book to be deleted because here we are maintaining relationship
    imprint = models.CharField(max_length=100)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintanence'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='m')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f"{self.id}, {self.book.title}"


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



