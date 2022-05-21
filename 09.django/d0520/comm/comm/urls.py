from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('member/', include('member.urls')),
     # freeboard app연결
    path('freeboard/',include('freeboard.urls')),
]
