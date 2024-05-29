from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

class Category(models.Model):
    category_name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length = 100)
    publisher = models.CharField(max_length = 100)
    publication = models.DateField(null=True, blank = True)
    isbn = models.CharField(max_length = 13, null = True, blank = True)
    shelf_number = models.CharField(max_length = 50, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

class Member(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    registration_date = models.DateField()

class Loan(models.Model):
    loan_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    member = models.ForeignKey(Member, on_delete = models.CASCADE)

class Staff(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

