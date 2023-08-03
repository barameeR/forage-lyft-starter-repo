from tire.tire import Tire

class OctoprimeTire(Tire):
    def needs_service(self):
        return sum(self.tire_ware) >= 3