# encounters will be generated when the player moves to a new node


class Encounter():
    def __init__(self):
        self.encounter_exists = True
    
    def check_encounter_generation(self):
        if self.encounter_exists:
            return "encounter has been generated properly"
        