import sys
sys.path.append('../')
from datetime import datetime
from car_factory import CarFactory

if __name__ == '__main__':
    car_factory = CarFactory()
    today = datetime.today().date()
    last_service_date = today.replace(year=today.year - 1)
    current_mileage = 10000
    last_service_mileage = 0
    tire_ware = [0.8,0.8,0.8,0.8]

    car1 = car_factory.create_calliope(today,last_service_date,current_mileage,last_service_mileage,tire_ware)

    result = car1.needs_service()
    print(result)
    