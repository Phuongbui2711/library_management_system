from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from datetime import datetime,timedelta


class UserExtend(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone = CharField(max_length=45)
    def __str__(self):
       return self.user.username


class Member(models.Model):
    user = models.ForeignKey(User,unique=False,on_delete=models.CASCADE)
    member_id=models.CharField(max_length=45)
    name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    phone=models.CharField(max_length=45)
    def __str__(self):
        return self.member_id


class Author(models.Model):
    author_id = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    def __str__(self):
        return self.name


class Category(models.Model):
    type = models.CharField(max_length=45)
    def __str__(self):
        return self.type


class Publisher(models.Model):
    name = models.CharField(max_length=45)
    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(User, unique=False,on_delete=models.CASCADE)
    isbn = models.CharField(max_length=45)
    title=CharField(max_length=255)
    status = models.CharField(max_length=45)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    def __str__(self):
        return self.isbn


def expiry():
    return datetime.today() + timedelta(days=15)

class Order(models.Model):
    user = models.ForeignKey(User, unique=False,on_delete=models.CASCADE)
    startTime = models.DateField(auto_now=True)
    returnTime = models.DateField(default=expiry)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

class Return(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete= models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)