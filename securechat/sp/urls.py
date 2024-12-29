from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.chat_view,name='chat_view'),
    path('delete_chats/', views.delete_chats, name='delete_chats'),
  
]
