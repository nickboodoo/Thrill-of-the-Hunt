# the conductor: decides when to update, when to render text, and when to stop
# i want game class to generate a map instance

from engine.world import World
from actors.player import Player
from actors.enemy import Enemy
from events.encounter import Encounter

class Game():
    def __init__(self):
        self.running = True
    
    def run(self):
        if self.running:
            print("Game is running")
            overworld = World()
            print(World().generate_map(4))
            print(Player().check_player_generation())
            print(Enemy().check_enemy_exist())
            print(Encounter().check_encounter_generation())

