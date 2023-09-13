from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear_sensors_values):
        self.wear_sensors_values = wear_sensors_values

    def needs_service(self):
        result = False
        for val in self.wear_sensors_values:
            if val >= 0.9:
                result = True
                break
        return result
