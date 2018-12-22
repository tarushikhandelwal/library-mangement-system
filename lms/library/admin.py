from django.contrib import admin
from . models import book,issuedetail,returndetail,User

admin.site.register(book)
admin.site.register(issuedetail)
admin.site.register(returndetail)
admin.site.register(User)