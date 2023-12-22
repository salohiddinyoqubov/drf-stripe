from django.urls import path

from .views import get_buy

urlpatterns = [
    path('<int:pk>/', get_buy, name='buy')
]
