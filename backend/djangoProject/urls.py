from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings

urlpatterns = [# path('/', admin.site.urls),
               path('api/', include('app.urls')),
               ]
