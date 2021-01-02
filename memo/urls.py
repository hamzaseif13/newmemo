from . import views 
from django.urls import path

app_name='memo'
urlpatterns=[
    path('day/<str:pk>/',views.day,name='day'),
    path('',views.home,name="home")
]