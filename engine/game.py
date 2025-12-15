# the conductor: decides when to update, when to render text, and when to stop

class Game():
    def __init__(self):
        self.running = True
    
    def run(self):
        if self.running:
            print("Game is running")