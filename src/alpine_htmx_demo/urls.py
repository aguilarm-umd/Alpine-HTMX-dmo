from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("replace", views.replace, name="replace"),
    path("send_message", views.send_message, name="send_message"),
]
