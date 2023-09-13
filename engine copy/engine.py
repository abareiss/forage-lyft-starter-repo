from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class Engine():
    def __init__(self, engine_type):
        self.engine_type = engine_type
        
    def needs_service(self):
        return self.engine_type.needs_service()
