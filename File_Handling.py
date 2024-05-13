class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
    
    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.name},{self.floors}\n")
    
    @staticmethod
    def load_from_file(filename):
        buildings = []
        with open(filename, 'r') as file:
            for line in file:
                name, floors = line.strip().split(',')
                buildings.append(Building(name, int(floors)))
        return buildings


building1 = Building("Skyscraper A", 30)
building2 = Building("Office Complex B", 10)
building3 = Building("Residential Tower C", 20)

# Save buildings to file
building1.save_to_file("buildings.txt")
building2.save_to_file("buildings.txt")
building3.save_to_file("buildings.txt")

# Load buildings from file
loaded_buildings = Building.load_from_file("buildings.txt")

# Display loaded buildings
print("Loaded Buildings:")
for building in loaded_buildings:
    print("Name:", building.name, "| Floors:", building.floors)
