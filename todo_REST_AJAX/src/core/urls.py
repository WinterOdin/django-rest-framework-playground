from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
	path('', views.home, name='test'),
    path('taskList/', views.taskList, name='task'),
    path('taskDetail/<str:pk>/', views.detailView, name='taskDetail'),
    path('createTask/', views.createView, name='createTask'),
    path('updateTask/<str:pk>/', views.updateView, name='updateView'),
    path('deleteTask/<str:pk>/', views.deleteView, name='deleteView'),
]