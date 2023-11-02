from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import worldgen
import menu


app = Ursina()

menu.mainMenu()


app.run()
