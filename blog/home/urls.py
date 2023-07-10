from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup,name="signup"),
    path('userlogin', views.userlogin,name="userlogin"),
    path('userlogout', views.userlogout, name="userlogout"),

]
