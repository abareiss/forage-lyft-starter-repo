from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wear_sensors_values):
        self.wear_sensors_values = wear_sensors_values

    def needs_service(self):
        total = 0 
        for val in self.wear_sensors_values:
            total += val
        return total >= 3