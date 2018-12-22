
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',include('library.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_ROOT=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_ROOT=settings.MEDIA_ROOT)