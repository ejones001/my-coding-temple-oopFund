class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner
    
    def update_owner(self, new_owner):
        self.owner = new_owner

# Creating instances of Vehicle
vehicle1 = Vehicle("ABC123", "Car", "John")
vehicle2 = Vehicle("XYZ456", "Truck", "Alice")
vehicle3 = Vehicle("DEF789", "Motorcycle", "Bob")

# Demonstrate changing the owner
print("Original owners:")
print("Vehicle 1 owner:", vehicle1.owner)
print("Vehicle 2 owner:", vehicle2.owner)
print("Vehicle 3 owner:", vehicle3.owner)

vehicle1.update_owner("Michael")
vehicle2.update_owner("Emma")

print("\nUpdated owners:")
print("Vehicle 1 owner:", vehicle1.owner)
print("Vehicle 2 owner:", vehicle2.owner)
print("Vehicle 3 owner:", vehicle3.owner)
