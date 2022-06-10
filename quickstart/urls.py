
from django.urls import path
from . import views


urlpatterns = [
    path("users/",views.MyUserView.as_view())
]