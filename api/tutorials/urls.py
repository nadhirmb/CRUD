from tutorials import views 
from django.urls import path
 
urlpatterns = [ 
    path('api/tutorials', views.tutorial_list),
]