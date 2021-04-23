from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.index,name="index"),
    path('register', views.register, name="register"),
    path('successL', views.successL, name="successL"),
    path('login', views.login, name="login"),
]
