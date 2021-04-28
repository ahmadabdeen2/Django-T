from django.urls import path 
from userauthen import views

app_name= "userauthen"

urlpatterns=[
    path('register/' , views.register, name = 'register'),
      path("login/", views.user_login, name = "userlogin"),
]