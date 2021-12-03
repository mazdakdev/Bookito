
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('User.urls')),
    path('api/v1/auth/', include('knox.urls')),
    path('api/v1/books/', include('books.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)