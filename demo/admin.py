from django.contrib import admin
from .models import Author, Books

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'name', 'birthdate')


admin.site.register(Author, AuthorAdmin)