import main
class Hunter:
    def __init__(self, name):
        self.species = name
        self.strength = 1
        self.intelligence = 2
        self.wisdom = 3
        self.speed = 4

class Species:
    def __init__(self, name):
        self.species = name
        self.strength = 1
        self.intelligence = 2
        self.wisdom = 3
        self.speed = 4
hunter1 = Hunter("Hunter1")

assert main.compare_skills(Hunter("Hunter"), Species('Mammoth')) == None
assert main.get_total_skills(hunter1) == 10
main.increase_stats(hunter1)
assert main.compare_skills(hunter1, Species('Mammoth')) is hunter1
assert len(main.create_animals()) == 5

