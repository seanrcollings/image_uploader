from django.urls import path, re_path

from . import views

app_name = 'image_post'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('new', views.CreatePost.as_view(), name='new'),
    path('search/', views.search, name='search'),
    path('<int:image_post_id>/vote', views.vote, name='vote'),
    
]