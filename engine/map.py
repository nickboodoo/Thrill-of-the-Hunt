


class Map():
    def __init__(self, size):
        self.map_exists = True
        self.size = 2

    def check_map_existance(self):
        if self.map_exists:
            return f"map is successfully generated with {self.size} nodes"