from django.urls import path

from . import views

urlpatterns = [
    path('job', views.job, name='job'),
    path('detail', views.detail, name='detail'),
    path('results', views.results, name='results'),
    path('vote', views.vote, name='vote'),
]