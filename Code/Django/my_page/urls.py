from django.urls import path
from .views import *

app_name='my_page'

urlpatterns = [
    path('', index, name='index'),
    path('most_similar_job/', go_to_most_similar_job, name='most_similar_job'),
]