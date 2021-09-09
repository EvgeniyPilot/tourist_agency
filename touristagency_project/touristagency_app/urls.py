from django.urls import path
from .views import *

urlpatterns = [
    path('clients/', ClientsLists.as_view()),
    path('clients/<int:id>/', ClientDetailView.as_view()),
    path('posts/', PostsListView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('emloys/', EmployListView.as_view()),
    path('emloys/<int:pk>/', EmployDetailView.as_view()),
]