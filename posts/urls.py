from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.posts_home, name='posts-home'),
    path('<int:post_id>/', views.posts_detail, name='posts-detail'),
]
