from typing import List

from models import Vehicle, vehicle_db, engine_db, Engine


class VehicleService:
    def get_vehicles_with_current_type(self, vehicle_type: str) -> List[Vehicle]:
        return list(filter(lambda vehicle: vehicle.type_of_vehicle.value == vehicle_type, vehicle_db))
    
    def get_vehicle_by_name(self, name: str) -> Vehicle:
        for vehicle in vehicle_db:
            if vehicle.name == name:
                return vehicle
            
    def create_car(self, car: Vehicle) -> Vehicle:
        vehicle_db.append(car)
        return car
    
    def get_random_vehicle(self) -> Vehicle:
        return Vehicle(name='-', weight=0.0, range_of_movement=0.0)

    @staticmethod    
    def get_service() -> 'VehicleService':
        return VehicleService()


class EngineService:
    def get_engines(self) -> List[Engine]:
        return engine_db
    
    def add_engine(self, engine: Engine) -> Engine:
        engine_db.append(engine)
        return engine

    @staticmethod
    def get_service() -> Engine:
        return EngineService()
