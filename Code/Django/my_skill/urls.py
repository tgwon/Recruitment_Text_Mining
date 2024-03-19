from django.urls import path
from .views import *

app_name='my_skill'

urlpatterns = [
    path('', index, name='index'),
    path('graph/', show_total_graph, name='show_total_graph'),
]
