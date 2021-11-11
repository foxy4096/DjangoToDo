from django.urls import path

from . import views

urlpatterns = [
	path('', views.ToDoListView.as_view(), name='home'),
    path('add/', views.ToDoCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', views.ToDoUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.ToDoDeleteView.as_view(), name='delete')
]