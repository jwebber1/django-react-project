from django.shortcuts import render
from rest_framework import generics, status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# These are the endpoints

class BeastView(generics.ListCreateAPIView):
  queryset = Beast.objects.all()
  serializer_class = BeastSerializer

class ItemView(generics.ListCreateAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer

class NpcView(generics.ListCreateAPIView):
  queryset = Entity.objects.all()
  serializer_class = NpcSerializer

class CharacterView(generics.ListCreateAPIView):
  queryset = Character.objects.all()
  serializer_class = CharacterSerializer

class CreateCharacterView(APIView):
  serializer_class = CreateCharacterSerializer

  def post(self, request, format=None):
    if not self.request.session.exists(self.request.session.session_key):
      self.request.session.create()
    
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      char_name = serializer.data.get('name')
      queryset = Character.objects.filter(name=char_name)
      if queryset.exists():
        character = queryset[0]
        character.is_member = serializer.data.get('is_member')
        character.agility = serializer.data.get('agility')
        character.agility_xp = serializer.data.get('agility_xp')
        character.archaeology = serializer.data.get('archaeology')
        character.archaeology_xp = serializer.data.get('archaeology_xp')
        character.attack = serializer.data.get('attack')
        character.attack_xp = serializer.data.get('attack_xp')
        character.constitution = serializer.data.get('constitution')
        character.constitution_xp = serializer.data.get('constitution_xp')
        character.construction = serializer.data.get('construction')
        character.construction_xp = serializer.data.get('construction_xp')
        character.cooking = serializer.data.get('cooking')
        character.cooking_xp = serializer.data.get('cooking_xp')
        character.crafting = serializer.data.get('crafting')
        character.crafting_xp = serializer.data.get('crafting_xp')
        character.defence = serializer.data.get('defence')
        character.defence_xp = serializer.data.get('defence_xp')
        character.divination = serializer.data.get('divination')
        character.divination_xp = serializer.data.get('divination_xp')
        character.dungeoneering = serializer.data.get('dungeoneering')
        character.dungeoneering_xp = serializer.data.get('dungeoneering_xp')
        character.farming = serializer.data.get('farming')
        character.farming_xp = serializer.data.get('farming_xp')
        character.firemaking = serializer.data.get('firemaking')
        character.firemaking_xp = serializer.data.get('firemaking_xp')
        character.fishing = serializer.data.get('fishing')
        character.fishing_xp = serializer.data.get('fishing_xp')
        character.fletching = serializer.data.get('fletching')
        character.fletching_xp = serializer.data.get('fletching_xp')
        character.herblore = serializer.data.get('herblore')
        character.herblore_xp = serializer.data.get('herblore_xp')
        character.hunter = serializer.data.get('hunter')
        character.hunter_xp = serializer.data.get('hunter_xp')
        character.invention = serializer.data.get('invention')
        character.invention_xp = serializer.data.get('invention_xp')
        character.magic = serializer.data.get('magic')
        character.magic_xp = serializer.data.get('magic_xp')
        character.mining = serializer.data.get('mining')
        character.mining_xp = serializer.data.get('mining_xp')
        character.prayer = serializer.data.get('prayer')
        character.prayer_xp = serializer.data.get('prayer_xp')
        character.ranged = serializer.data.get('ranged')
        character.ranged_xp = serializer.data.get('ranged_xp')
        character.runecrafting = serializer.data.get('runecrafting')
        character.runecrafting_xp = serializer.data.get('runecrafting_xp')
        character.slayer = serializer.data.get('slayer')
        character.slayer_xp = serializer.data.get('slayer_xp')
        character.smithing = serializer.data.get('smiting')
        character.smithing_xp = serializer.data.get('smithing_xp')
        character.strength = serializer.data.get('strength')
        character.strength_xp = serializer.data.get('strength_xp')
        character.summoning = serializer.data.get('summoning')
        character.summoning_xp = serializer.data.get('summoning_xp')
        character.thieving = serializer.data.get('thieving')
        character.thieving_xp = serializer.data.get('thieving_xp')
        character.woodcutting = serializer.data.get('woodcutting')
        character.woodcutting_xp = serializer.data.get('woodcutting_xp')

        character.save(update_fields=[
          'is_member', 'agility', 'archaeology', 'attack', 'constitution', 'construction', 'cooking', 'crafting', 'defence', 'divination', 'dungeoneering', 'farming', 'firemaking', 'fishing', 'fletching', 'herblore', 'hunter', 'invention', 'magic', 'mining', 'prayer', 'ranged', 'runecrafting', 'slayer', 'smithing', 'strength', 'summoning', 'thieving', 'woodcutting',
          'agility_xp', 'archaeology_xp', 'attack_xp', 'constitution_xp', 'construction_xp', 'cooking_xp', 'crafting_xp', 'defence_xp', 'divination_xp', 'dungeoneering_xp', 'farming_xp', 'firemaking_xp', 'fishing_xp', 'fletching_xp', 'herblore_xp', 'hunter_xp', 'invention_xp', 'magic_xp', 'mining_xp', 'prayer_xp', 'ranged_xp', 'runecrafting_xp', 'slayer_xp', 'smithing_xp', 'strength_xp', 'summoning_xp', 'thieving_xp', 'woodcutting',
        ])
      else:
        character = Character(
          name = char_name,
          is_member = serializer.data.get('is_member'),
          agility = serializer.data.get('agility'),
          agility_xp = serializer.data.get('agility_xp'),
          archaeology = serializer.data.get('archaeology'),
          archaeology_xp = serializer.data.get('archaeology_xp'),
          attack = serializer.data.get('attack'),
          attack_xp = serializer.data.get('attack_xp'),
          constitution = serializer.data.get('constitution'),
          constitution_xp = serializer.data.get('constitution_xp'),
          construction = serializer.data.get('construction'),
          construction_xp = serializer.data.get('construction_xp'),
          cooking = serializer.data.get('cooking'),
          cooking_xp = serializer.data.get('cooking_xp'),
          crafting = serializer.data.get('crafting'),
          crafting_xp = serializer.data.get('crafting_xp'),
          defence = serializer.data.get('defence'),
          defence_xp = serializer.data.get('defence_xp'),
          divination = serializer.data.get('divination'),
          divination_xp = serializer.data.get('divination_xp'),
          dungeoneering = serializer.data.get('dungeoneering'),
          dungeoneering_xp = serializer.data.get('dungeoneering_xp'),
          farming = serializer.data.get('farming'),
          farming_xp = serializer.data.get('farming_xp'),
          firemaking = serializer.data.get('firemaking'),
          firemaking_xp = serializer.data.get('firemaking_xp'),
          fishing = serializer.data.get('fishing'),
          fishing_xp = serializer.data.get('fishing_xp'),
          fletching = serializer.data.get('fletching'),
          fletching_xp = serializer.data.get('fletching_xp'),
          herblore = serializer.data.get('herblore'),
          herblore_xp = serializer.data.get('herblore_xp'),
          hunter = serializer.data.get('hunter'),
          hunter_xp = serializer.data.get('hunter_xp'),
          invention = serializer.data.get('invention'),
          invention_xp = serializer.data.get('invention_xp'),
          magic = serializer.data.get('magic'),
          magic_xp = serializer.data.get('magic_xp'),
          mining = serializer.data.get('mining'),
          mining_xp = serializer.data.get('mining_xp'),
          prayer = serializer.data.get('prayer'),
          prayer_xp = serializer.data.get('prayer_xp'),
          ranged = serializer.data.get('ranged'),
          ranged_xp = serializer.data.get('ranged_xp'),
          runecrafting = serializer.data.get('runecrafting'),
          runecrafting_xp = serializer.data.get('runecrafting_xp'),
          slayer = serializer.data.get('slayer'),
          slayer_xp = serializer.data.get('slayer_xp'),
          smithing = serializer.data.get('smiting'),
          smithing_xp = serializer.data.get('smithing_xp'),
          strength = serializer.data.get('strength'),
          strength_xp = serializer.data.get('strength_xp'),
          summoning = serializer.data.get('summoning'),
          summoning_xp = serializer.data.get('summoning_xp'),
          thieving = serializer.data.get('thieving'),
          thieving_xp = serializer.data.get('thieving_xp'),
          woodcutting = serializer.data.get('woodcutting'),
          woodcutting_xp = serializer.data.get('woodcutting_xp')
        )
        character.save()

      return Response(CharacterSerializer(character).data, status=status.HTTP_201)