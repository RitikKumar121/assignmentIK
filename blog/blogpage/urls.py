from django.urls import path
from blogpage import views
urlpatterns = [
    path('',views.blogPage),
    path('<str:author>', views.blogPost, name="blogPost"),
]
