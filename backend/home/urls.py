from django.urls import path
from .views import HomeDetailView

urlpatterns = [
    path('', HomeDetailView.as_view(), name="home"),
]
