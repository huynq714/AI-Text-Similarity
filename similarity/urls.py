from django.urls import path
from . import views
from .api_views import generate_random_texts

urlpatterns = [
    path('', views.index, name='index'),
    path(
    'api/generate-texts/',
    generate_random_texts,
    name='generate_random_texts'
),
]
