from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogView, name="blogs"),
    path('<int:id>/', views.blogDetail, name="blog_detail"),
]