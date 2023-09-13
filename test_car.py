import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery

from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
class Tests(unittest.TestCase):
    def test_unservicable_nubbin_battery(self):
        # doesn't need service
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        self.nubbin_battery = NubbinBattery(last_service_date, datetime.today().date())
        self.assertFalse(self.nubbin_battery.needs_service(), "Should be False")

    def test_servicable_nubbin_battery(self):
        # needs service
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        self.nubbin_battery = NubbinBattery(last_service_date, datetime.today().date())
        self.assertTrue(self.nubbin_battery.needs_service(), "Should be True")

    def test_unserviceable_spindler_battery(self):
        # doesn't need service 
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        self.nubbin_battery = SpindlerBattery(last_service_date, datetime.today().date())
        self.assertFalse(self.nubbin_battery.needs_service(), "Should be False")

    def test_servicable_spindler_battery(self):
        # needs service
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        self.nubbin_battery = SpindlerBattery(last_service_date, datetime.today().date())
        self.assertTrue(self.nubbin_battery.needs_service(), "Should be True")

    def test_unservicable_capulet_engine(self):
        #doesn't need service
        capulet_engine = CapuletEngine(40000, 20000)
        self.assertFalse(capulet_engine.needs_service(), "Should be False")

    def test_servicable_capulet_engine(self):
        #needs service
        capulet_engine = CapuletEngine(60000, 20000)
        self.assertTrue(capulet_engine.needs_service(), "Should be True")

    def test_unservicable_sternman_engine(self):
        #doesn't need service
        sternman_engine = SternmanEngine(False)
        self.assertFalse(sternman_engine.needs_service(), "Should be False")

    def test_servicable_sternman_engine(self):
        #need service
        sternman_engine = SternmanEngine(True)
        self.assertTrue(sternman_engine.needs_service(), "Should be True")

    def test_unservicable_willoughby_engine(self):
        #doesn't need service
        willoughby_engine = WilloughbyEngine(40000, 20000)
        self.assertFalse(willoughby_engine.needs_service(), "Should be False")

    def test_servicable_willoughby_engine(self):
        #need service
        willoughby_engine = WilloughbyEngine(100000, 20000)
        self.assertTrue(willoughby_engine.needs_service(), "Should be True")

    def test_unserviceable_carrigan_tires(self):
        carrigan_tire = CarriganTire([0, 0, 0, 0])
        self.assertFalse(carrigan_tire.needs_service(), "Should be False")
    
    def test_serviceable_carrigan_tires(self):

        carrigan_tire = CarriganTire([0, 0, 0.9, 0])
        self.assertTrue(carrigan_tire.needs_service(), "Should be True")

    def test_unserviceable_octoprime_tires(self):
        octoprime_tire = OctoprimeTire([0, 0, 0, 0])
        self.assertFalse(octoprime_tire.needs_service(), "Should be False")

    def test_serviceable_octoprime_tires(self):
        octoprime_tire = OctoprimeTire([1, 1, 1, 0])
        self.assertTrue(octoprime_tire.needs_service(), "Should be True")

if __name__ == '__main__':
    unittest.main()
