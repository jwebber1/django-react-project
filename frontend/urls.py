from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('beasts', index),
    path('character', index),
    path('items', index),
    path('skills', index),
]
