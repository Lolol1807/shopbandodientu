from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('detail/<int:id>',views.Detail,name='detail'),
]
