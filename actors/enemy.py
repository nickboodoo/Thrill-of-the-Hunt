# enemy class that will play against player

class Enemy():
    def __init__(self):
        self.enemy_exists = True
    
    def check_enemy_exist(self):
        if self.enemy_exists:
            return "enemy exists"