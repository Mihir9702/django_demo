from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # username
    path('post/<str:pk>', views.post, name='post'),
    path('posts', views.posts, name='posts')
    # userid
    # path('post/<int:pk>', views.post, name='post')
]
