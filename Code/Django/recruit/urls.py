from django.urls import path, re_path
from . import views

app_name = 'recruit'

urlpatterns = [
    path('', views.RecruitList.as_view(), name='index'),
    path('<int:pk>/', views.RecruitDetail.as_view(), name='detail'),
]