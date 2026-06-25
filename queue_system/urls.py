from django.urls import path
from . import views

urlpatterns = [

    path('join/', views.join_queue, name='join_queue'),

    path('my-queue/', views.my_queue, name='my_queue'),

    path('live/', views.live_queue, name='live_queue'),

]