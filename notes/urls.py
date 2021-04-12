from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createNote', views.createNote, name='createNote'),
    path('tagList', views.tagList, name='tagList'),
    path('updateNote/<str:pk>/', views.updateNote, name='updateNote'),
    path('deleteNote/<str:pk>/', views.deleteNote, name='deleteNote'),

]