from tire.tire import Tire

class CarriganTire(Tire):
    def needs_service(self):
        return any(wear >= 0.9 for wear in self.tire_ware)