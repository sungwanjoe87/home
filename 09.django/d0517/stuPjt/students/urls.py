from django.urls import path,include
from . import views

app_name='students'
urlpatterns = [
    path('stuWrite', views.stuWrite, name='stuWrite'), #학생등록 페이지
    path('stuList', views.stuList, name='stuList'), #학생리스트 페이지
    path('<str:name>/<str:major>/stuView', views.stuView, name='stuView'), #학생상세 페이지
]
