from . import views
from django.urls import path


urlpatterns = [
    path("", views.index),
    path("function-view/", views.postuser, name ='postuser')
]
