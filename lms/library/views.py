from django import http
from datetime import timedelta
from .models import book, issuedetail, returndetail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import UserForm, UserLoginForm, IssueDetailForm
from django.contrib.auth import get_user_model
from django.shortcuts import render
from simple_search import search_filter
from datetime import datetime, date

User = get_user_model()


def home(request):
    return render(request, 'library/home.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'library/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user.listbook = []
            return redirect('library:registered')

        return render(request, self.template_name, {'form': form})


def registered(request):
    return render(request, 'library/registered.html')


class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'library/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
            return redirect('library:book')

        return render(request, self.template_name, {'form': form})


class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']


class BookCreate(CreateView):
    model = book
    fields = ['title', 'subject', 'authorname', 'price', 'edition', 'bookimg']


class BookUpdate(UpdateView):
    model = book
    fields = ['title', 'subject', 'authorname', 'price', 'edition', 'bookimg']


class BookDelete(DeleteView):
    model = book
    template_name = 'library/delete.html'
    context_object_name = 'books'
    success_url = reverse_lazy('library:book')


class IndexView(generic.ListView):
    template_name = 'library/book.html'
    context_object_name = 'allbook'

    def get_queryset(self):
        return book.objects.all()


class DetailViewUser(generic.DetailView):
    model = User
    template_name = 'library/detailuser.html'


class DetailView(generic.DetailView):
    model = book
    template_name = 'library/detail.html'


def searchh(request):
    search_fields = ['title', 'subject', 'edition', 'authorname']
    query = request.GET['q']
    posts = book.objects.filter(search_filter(search_fields, query))

    return render(request, 'library/result.html', {'posts': posts})


class IssueDetailView(View):
    form_class = IssueDetailForm
    template_name = 'library/issuedetail_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        Book = request.POST.get('Book')
        issuedate = date.today()
        userid = request.user.id
        p1 = issuedetail(Book=Book, issuedate=issuedate, userid=userid)
        allbook = book.objects.filter(id=Book)
        if len(allbook) > 0:
            # User.listbook.append(Book)
            p1.save()
            return redirect('library:success')
        else:
            return redirect('library:failed')

        return render(request, self.template_name, {'form': form})


def sucess(request):
    return render(request, 'library/success.html')


def failed(request):
    return render(request, 'library/failed.html')


def detailview(request):
    allissues = issuedetail.objects.filter(userid=User.pk)
    if len(allissues) > 0:
        return render(request, 'library:detailuser')
    else:
        return render(request, 'library:Noissues')


def logoutr(request):
    logout(request)
    return redirect('library:home')


def Detailuser(request):
    issue = issuedetail.objects.filter(userid=request.user.id)
    return render(request, 'library/detailuser.html', {'issue': issue})


def fine(issuepk):
    t = issuedetail.objects.filter(id=issuepk)
    for M in t:
        delta = date.today() - M.issuedate
        if delta.days > 7:
            User.dfee += 5 * (7 - delta.days)
            User.save()


class IssueDetailDelete(DeleteView):
    model = issuedetail
    template_name = 'library/return.html'
    context_object_name = 'returnbook'

    def delete(self, request, *args, **kwargs):
        issued = self.get_object()
        issuepk = issued.pk
        fine(issuepk)
        issued.delete()
        success_url = reverse_lazy('library:detailuser')
        return render(request,'library/detailuser.html')

def issuelist(request):
    issue = issuedetail.objects.filter()
    return render(request, 'library/issuelist.html', {'issue': issue})


def alluser(request):
    AllUser = User.objects.all()
    return render(request, 'library/alluser.html', {'AllUser': AllUser})
