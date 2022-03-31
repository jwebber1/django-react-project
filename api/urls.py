from django.urls import path
from .views import *

urlpatterns = [
    path('beasts', BeastView.as_view()),
    path('items', ItemView.as_view()),
    path('npc', NpcView.as_view()),
    path('character', CharacterView.as_view()),
    path('skills', SkillsView.as_view()),
]
