from battery.battery import Battery
from engine.engine import Engine

class Serviceable():
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return (self.engine.needs_service() and self.battery.needs_service())