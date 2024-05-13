class Bus:
    city_name = "CityX"
    base_fare = 2.50
    
    def __init__(self, route_number, passenger_capacity):
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity


bus1 = Bus(101, 50)
bus2 = Bus(102, 40)

print("City Name:", Bus.city_name)
print("Base Fare:", Bus.base_fare)

print("\nBus 1 - Route Number:", bus1.route_number)
print("Bus 1 - Passenger Capacity:", bus1.passenger_capacity)

print("\nBus 2 - Route Number:", bus2.route_number)
print("Bus 2 - Passenger Capacity:", bus2.passenger_capacity)
