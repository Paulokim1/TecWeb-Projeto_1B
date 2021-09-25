from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
    path('viewTagList', views.viewTagList, name='viewTagList'),
    path('viewTags', views.viewTags, name='viewTagPage') 
]