from django.urls import path
from . import views
from .views import logout

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register , name='register'),
    path("logout", logout.as_view(), name="logout")
]
