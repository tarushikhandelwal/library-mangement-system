from library import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'library'
urlpatterns = [

    path('registered', views.registered, name='registered'),
    path('', views.home, name='home'),
    path('signin/', views.UserFormView.as_view(), name='signin'),
    path('success/', views.sucess, name='success'),
    path('failed/', views.failed, name='failed'),
    path('login/', views.UserLoginFormView.as_view(), name='login'),
    path('book/', views.IndexView.as_view(), name='book'),
    path('detail/<int:pk>/', views.DetailViewUser.as_view(), name='detail'),
    path('detailuser/', views.Detailuser, name='detailuser'),
    path('search/', views.searchh, name='search'),
    path('book/issue/', views.IssueDetailView.as_view(), name='issuebook'),
    path('book/create/', views.BookCreate.as_view(), name='bookcreate'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='updatebook'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='deletebook'),
    path('book/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('book/<int:pk>/<int:userid>/', views.DetailView.as_view(), name='detail'),
    path('logout/', views.logoutr, name="logout"),
    path('issuedetail/<int:pk>/delete/', views.IssueDetailDelete.as_view(), name="issuedetaildelete"),
    path('results/', views.searchh, name='searching'),
    path('UserUpdate/<int:pk>/', views.UserUpdate.as_view(), name='UserUpdate'),
    path('issuelist/', views.issuelist, name='issuelist'),
    path('alluser/', views.alluser, name='alluser'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_ROOT=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_ROOT=settings.MEDIA_ROOT)
