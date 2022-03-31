from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# In general for django, we want large models (put logic and functions here) and thin views

class Entity(models.Model):
    name = models.CharField(max_length=100)
    membership_req = models.BooleanField(default=False)
    type = models.PositiveSmallIntegerField() #determines if an Entity is an NPC (0), Beast (1), or Item (2)

class Beast(Entity):
    attack_style = models.CharField(max_length=100, default='')
    weakness = models.CharField(max_length=100, default='')
    life_points = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)

class Item(Entity):
    price = models.PositiveIntegerField(default=1)

# Usernames must be between 1 and 12 characters long. Usernames may only contain alphanumeric characters, the space, and hyphens (-). Any other characters are replaced with a space.
# https://runescape.wiki/w/Character_name#Limitations 
class Character(models.Model):
    name = models.CharField(max_length=12, unique=True)
    is_member = models.BooleanField(default=False)

class Skills(models.Model):
    character_name = models.OneToOneField(Character, on_delete = models.CASCADE, primary_key = True)
    agility = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    archaeology = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    attack = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    constitution = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(120)])
    construction = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    cooking = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    crafting = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    defence = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    divination = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    dungeoneering = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    farming = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    firemaking = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    fishing = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    fletching = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    herblore = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    hunter = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    invention = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    magic = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    mining = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    prayer = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    ranged = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    runecrafting = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    slayer = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    smithing = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    strength = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    summoning = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    thieving = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
    woodcutting = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(120)])
