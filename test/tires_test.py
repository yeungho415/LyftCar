from tires.tires_type.carrigan_tires import CarriganTires
from tires.tires_type.octoprime_tires import OctoprimeTires

import unittest
import datetime


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [1, 0.1, 0.2, 0.3]
        battery = CarriganTires(tire_wear)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.1, 0.2, 0.3]
        battery = CarriganTires(tire_wear)
        self.assertFalse(battery.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [1, 1, 1, 0.5]
        battery = OctoprimeTires(tire_wear)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.1, 0.2, 0.3]
        battery = OctoprimeTires(tire_wear)
        self.assertFalse(battery.needs_service())