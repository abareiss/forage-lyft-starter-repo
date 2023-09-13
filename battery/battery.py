from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class Battery():
    def __init__(self, battery_type):
        self.battery_type = battery_type

    def needs_service(self):
        return self.battery_type.needs_service()