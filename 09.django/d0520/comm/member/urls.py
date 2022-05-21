from django.urls import path, include
from . import views

app_name = 'member'
urlpatterns = [
    # login페이지 연결
    path('login/',views.login,name='login'),
    # logout페이지 연결
    path('logout/',views.logout,name='logout'),
]
