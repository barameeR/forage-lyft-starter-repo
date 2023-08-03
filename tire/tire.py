from Serviceable import Serviceable

class Tire(Serviceable):
    def __init__(self,tire_ware):
        self.tire_ware = tire_ware
    
    def needs_service():
        raise NotImplementedError("Subclasses must implement this method")