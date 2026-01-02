# map class will own the world map
from actors.player import Player
from actors.enemy import Enemy
from events.encounter import Encounter


class World():
    def __init__(self):
        self.map_exists = True
    
    def generate_map(self, size):
        world = [] * size
        return f"Map has been generated of size {size}"
    
    def generate_player(self):
        new_player = Player()
        print(new_player.check_player_generation())

    def generate_enemy(self):
        new_enemy = Enemy()
        print(new_enemy.check_enemy_exist())

    def generate_encounter(self):
        new_encounter = Encounter()
        print(new_encounter.check_encounter_generation())
    