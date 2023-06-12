from car import Car

from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.sternman_engine import SternmanEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine


class CarFactory:
    @staticmethod
    def create_calliope(current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        car = Car(engine)
        return car

    @staticmethod
    def create_glissade(current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car = Car(engine)
        return car

    @staticmethod
    def create_palindrome(warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        car = Car(engine)
        return car

    @staticmethod
    def create_rorschach(current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car = Car(engine)
        return car

    @staticmethod
    def create_thovex(current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        car = Car(engine)
        return car
