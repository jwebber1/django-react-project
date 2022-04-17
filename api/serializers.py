from rest_framework import serializers
from .models import *

class BeastSerializer(serializers.ModelSerializer):
  class Meta:
      model = Beast
      fields = '__all__' #('id', 'name', 'membership_req', 'type', 'attack_style', 'weakness', 'life_points', 'level')

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
      model = Item
      fields = '__all__' #('id', 'name', 'membership_req', 'type', 'price')

class NpcSerializer(serializers.ModelSerializer):
  class Meta:
      model = Entity
      fields = '__all__' #('id', 'name', 'membership_req', 'type')

class CharacterSerializer(serializers.ModelSerializer):
  class Meta:
      model = Character
      fields = '__all__' #('id', 'name', 'is_member', 'agility','archaeology','attack', 'constitution', 'construction', 'cooking', 'crafting', 'defence', 'divination', 'dungeoneering', 'farming', 'firemaking', 'fishing', 'fletching', 'herblore', 'hunter', 'invention', 'magic', 'mining', 'prayer', 'ranged', 'runecrafting', 'slayer', 'smithing', 'strength', 'summoning', 'thieving', 'woodcutting')

class CreateCharacterSerializer(serializers.ModelSerializer):
  class Meta:
      model = Character
      fields = ('name')