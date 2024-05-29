from django.contrib import admin
from .models import Author, Category, Book, Member, Loan, Staff

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Loan)
admin.site.register(Staff)


