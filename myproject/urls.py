from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('services/', include('app2.urls')),
    path('news/', include('app3.urls')),
]