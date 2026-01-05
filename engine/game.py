# the conductor: decides when to update, when to render text, and when to stop
# i want game class to generate a map instance

from engine.router import Router

class Game():
    def __init__(self):
        self.running = True
    
    def run(self):
        if self.running:
            print("Game is running")
            overworld = Router()
            print(Router().generate_map(4))
            print(Router().generate_player())
            print(Router().generate_enemy())
            print(Router().generate_encounter())

