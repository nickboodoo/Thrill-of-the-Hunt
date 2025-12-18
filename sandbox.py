class Location:
    def __init__(self, location_id, name):
        self.id = location_id
        self.name = name
        self.exits = {}

class World:
    def __init__(self):
        self.world_map = {}
        self.current_location_id = 1
    
        self.world_map[1] = Location(1, "Starting Location")
        self.world_map[2] = Location(2, "Room 2")
        self.world_map[3] = Location(3, "Room 3")

        self.world_map[1].exits["north"] = 2
        self.world_map[1].exits["south"] = 3

        self.world_map[2].exits["south"] = 1
        self.world_map[3].exits["north"] = 1
    
    def describe_location(self):
        location = self.world_map[self.current_location_id]
        exits = ", ".join(location.exits.keys()) if location.exits else "none"
        return f"You are in {location.name}\nExits: {exits}"
    
    def move_player(self, direction):
        location = self.world_map[self.current_location_id]
        if direction not in location.exits:
            return "You cannot go that way"
        
        self.current_location_id = location.exits[direction]
        return f"You go {direction}"
    
class Game:
    def __init__(self):
        self.running = True
        self.world = World()

        self.actions = {
            "north": lambda: self.world.move_player("north"),
            "south": lambda: self.world.move_player("south"),
            "look": self.world.describe_location,
            "quit": self.quit_game
            
        }
    
    def quit_game(self):
        self.running = False
        return "Goodbye"
    
    def run(self):
        while self.running:
            print(self.world.describe_location())

            command = input("> ").strip().lower()
            if command in self.actions:
                result = self.actions[command]()
                if result:
                    print(result)
            else:
                print("Commands: north, south, look, quit")

        print()
    

if __name__ == "__main__":
    print("SANDBOX TESTING")

    #Game().run()

    nums = [0, 1, 2]
    print(range(len(nums)))
