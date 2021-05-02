from django.contrib import admin

from .models import Books,Authors

class BooksAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'book_price', 'authors')
    list_display_links = ('book_title',)
    search_fields = ('book_title',)

admin.site.register(Books, BooksAdmin)
admin.site.register(Authors)
