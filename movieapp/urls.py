from django.urls import path
from . import views

app_name = 'movieapp'

urlpatterns = [
    path('', views.demo, name='demo'),
    path('detail/<int:movie_id>/', views.details, name='details'),
    path('add', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
