# crawler/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('crawl/', views.crawl, name='crawl'),
    path('show-pages/', views.show_pages, name='show_pages'),
]
