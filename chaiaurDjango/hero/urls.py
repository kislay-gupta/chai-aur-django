
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.all_hero,name="all_hero"),
    # path("order/", views.order,name="order"),
  
]
