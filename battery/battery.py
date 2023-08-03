from Serviceable import Serviceable

class Battery(Serviceable):
    def __init__(self) -> None:
        super().__init__()
    
    def needs_service(self):
        raise NotImplementedError("Subclasses must implement this method")