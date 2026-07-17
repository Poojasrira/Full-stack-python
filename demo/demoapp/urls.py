from django.urls import path
from .import views

urlpatterns = [
    path('',views.hello_world),
    path('India',views.HelloIndia.as_view()),
    path('reservation',views.home)
]