from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list' ),
    path('update_task/<str:pk>/', views.update, name='update_task')
]