"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from task_manager.users import views

urlpatterns = [
    path('', views.UsersView.as_view(),
         name='users-index'),
    path('create/', views.UsersCreateView.as_view(),
         name='users-create'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(),
         name='user-update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(),
         name='user-delete'),
]
