from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# l'utiliser pour mettre une pause en chargement pour éviter un bug
def waiting():
    pass


def gamesStart():
    ground = Entity(model='cube', collider='box', scale=64, texture='grass', texture_scale=(4,4))
    player = FirstPersonController()
