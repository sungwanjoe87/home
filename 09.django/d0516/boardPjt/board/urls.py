from . import views
from django.urls import path, include

app_name='board'
urlpatterns = [
    path('boardlist',views.boardlist, name='bdlist'),
]