from django.urls import path
from . import views

app_name = "little_bee"

urlpatterns = [
    path("",views.home_page,name="home")
]