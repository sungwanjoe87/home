from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
     # index 메인페이지 연결.
    path('', include('home.urls')),
     # member app연결.
    path('member/', include('member.urls')),
     # freeboard app연결
    path('freeboard/',include('freeboard.urls')),
]
