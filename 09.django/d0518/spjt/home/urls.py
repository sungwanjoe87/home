from django.urls import include,path
from . import views

app_name='' # 메인페이지 home : index.html
urlpatterns = [
    path('',views.index,name='index')
]