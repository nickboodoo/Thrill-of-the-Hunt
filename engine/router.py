# map class will own the world map
from actors.player import Player
from actors.enemy import Enemy
from events.encounter import Encounter
from engine.map import Map


class Router():
    def __init__(self):
        self.router_exists = True
    
    def generate_map(self, size):
        new_map = Map(4)
        return new_map.check_map_existance()
    
    def generate_player(self):
        new_player = Player()
        return new_player.check_player_generation()

    def generate_enemy(self):
        new_enemy = Enemy()
        return new_enemy.check_enemy_exist()

    def generate_encounter(self):
        new_encounter = Encounter()
        return new_encounter.check_encounter_generation()