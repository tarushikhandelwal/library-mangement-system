from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from datetime import datetime


class book(models.Model):
    bookimg = models.ImageField(upload_to='book_image',blank=True)
    title = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    authorname = models.CharField(max_length=120)
    price = models.FloatField()
    edition=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('library:book')

    def __str__(self):
        return self.title + "  " + self.authorname


class User(AbstractUser):
    dfee = models.IntegerField(default=0)
    listbook = ArrayField(models.PositiveIntegerField(),null=True)

    def get_absolute_url(self):
        return reverse('library:detailuser')


class issuedetail(models.Model):
    Book = models.IntegerField()
    userid = models.PositiveIntegerField()
    issuedate = models.DateField(default=datetime.now().date(),blank=True)

    def get_absolute_url(self):
        return reverse('library:success')


class returndetail(models.Model):
    Issuedetail = models.ForeignKey(issuedetail,on_delete=models.CASCADE)
    returndetail = models.DateField()
    duefee = models.FloatField()


