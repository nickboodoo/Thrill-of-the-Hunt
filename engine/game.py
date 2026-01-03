# the conductor: decides when to update, when to render text, and when to stop
# i want game class to generate a map instance

from engine.world import World

class Game():
    def __init__(self):
        self.running = True
    
    def run(self):
        if self.running:
            print("Game is running")
            overworld = World()
            print(World().generate_map(4))
            print(World().generate_player())
            print(World().generate_enemy())
            print(World().generate_encounter())

