from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('detail/<slug:slug>', views.blog_detail,name='blog_detail'),
]