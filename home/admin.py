from django.contrib import admin
from .models import Member, Author, Category, Publisher, Book, Order, Return

# Register your models here.
from django.contrib.sessions.models import Session
admin.site.register(Session)

from .models import UserExtend
class AddUserAdmin(admin.ModelAdmin):
    list_display=("name", "email", "phone")
admin.site.register(UserExtend, AddUserAdmin)

class AddMemberAdmin(admin.ModelAdmin):
    list_display=("name","member_id", "email", "phone")
admin.site.register(Member,AddMemberAdmin)

class AddAuthorAdmin(admin.ModelAdmin):
    list_display=("author_id", "name")
admin.site.register(Author,AddAuthorAdmin)

class AddCategoryAdmin(admin.ModelAdmin):
    list_display=("type",)
admin.site.register(Category, AddCategoryAdmin)

class AddPublisherAdmin(admin.ModelAdmin):
    list_display=("name",)
admin.site.register(Publisher, AddPublisherAdmin)

class AddBookAdmin(admin.ModelAdmin):
    list_display=("isbn","title","author", "category", "publisher", "status")
admin.site.register(Book,AddBookAdmin)

class IssueBookAdmin(admin.ModelAdmin):
    list_display=("startTime", "returnTime","book","member")
admin.site.register(Order,IssueBookAdmin)

class ReturnBookAdmin(admin.ModelAdmin):
    list_display=("book", "member")
admin.site.register(Return,ReturnBookAdmin)