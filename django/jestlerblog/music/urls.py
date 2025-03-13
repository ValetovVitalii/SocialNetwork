from django.urls import path,include
from music import views


urlpatterns = [

    path('', views.index),
    path('cats/<int:cat_id>/', views.categories)
]