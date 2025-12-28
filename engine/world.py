# map class will own the world map
from actors.player import Player

class World():
    def __init__(self):
        self.map_exists = True
    
    def generate_map(self, size):
        world = [] * size
        return f"Map has been generated of size {size}"
    
    def progress_player(self):
        # start player in starting room
        i = 0

    