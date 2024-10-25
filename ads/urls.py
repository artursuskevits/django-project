from django.urls import path
from .views import AdListView, AdDetailView, AdCreateView

urlpatterns = [
    path('', AdListView.as_view(), name='ad-list'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad-detail'),
    path('create/', AdCreateView.as_view(), name='ad-create'),
]
