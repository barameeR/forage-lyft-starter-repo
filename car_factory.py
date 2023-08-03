#import Car
from car import Car

#import Engines
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

#import Batteries
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

#import tires
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class CarFactory():
    
    @staticmethod
    def create_calliope( current_date, last_service_date, current_mileage, last_service_mileage,tire_ware):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        tire = CarriganTire(tire_ware)
        return Car(engine,battery,tire)
    
    @staticmethod
    def create_glissade( current_date, last_service_date, current_mileage, last_service_mileage,tire_ware):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        tire = CarriganTire(tire_ware)
        return Car(engine,battery,tire)
    
    @staticmethod
    def create_palindrome( current_date, last_service_date,warning_light_is_on,tire_ware):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date,current_date)
        tire = OctoprimeTire(tire_ware)
        return Car(engine,battery,tire)
    
    @staticmethod
    def create_rorschach( current_date, last_service_date, current_mileage, last_service_mileage,tire_ware):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        tire = OctoprimeTire(tire_ware)
        return Car(engine,battery,tire)
    
    @staticmethod
    def create_thovex( current_date, last_service_date, current_mileage, last_service_mileage,tire_ware):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        tire = OctoprimeTire(tire_ware)
        return Car(engine,battery,tire)