# player design

class Player():
    def __init__(self):
        self.player_exists = True
    
    def move_player(self, command):
        if self.player_exists:
            player_position += 1
            return "player moved"
