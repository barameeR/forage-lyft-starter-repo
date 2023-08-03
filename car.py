from abc import ABC
from Serviceable import Serviceable


class Car(Serviceable, ABC):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        engine_service = self.engine.needs_service()
        battery_service = self.battery.needs_service()
        tire_service = self.tire.needs_service()
        return engine_service or battery_service or tire_service
    
