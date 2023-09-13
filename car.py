from serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery

class Car():
    def __init__(self, engine_type, battery_type):
        self.engine = Engine(engine_type)
        self.battery = Battery(battery_type)

    def needs_service(self):
        self.servicable = Serviceable(self.engine, self.battery)
        return self.serviceable.needs_service()
