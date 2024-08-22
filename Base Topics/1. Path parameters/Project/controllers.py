from typing import List, Union

from fastapi import APIRouter, Depends

from models import TypeOfVehicle, Vehicle, Car, Ship, AirCraft, Engine
from services import VehicleService, EngineService

vehicle_router = APIRouter(prefix='/vehicles', tags=['transport'])

engine_router = APIRouter(prefix='/engines', tags=['engines'])


@vehicle_router.get('/my/')
async def get_my_vehicle():
    return 'My vehicle'


@vehicle_router.get('/cars/')
async def get_cars(vehicle_service: VehicleService = Depends(VehicleService.get_service)) -> List[Car]:
    response = vehicle_service.get_vehicles_with_current_type(TypeOfVehicle.GROUND.value)
    return response


# Данный контроллер приводит к исключению!
@vehicle_router.get('/danger/')
async def danger_example(vehicle_service: VehicleService = Depends(VehicleService.get_service)) -> Car:  # Аннотация указывает на Car
    response = vehicle_service.get_random_vehicle()
    return response  # Возвращается Vehicle!


@vehicle_router.post('/cars/')
async def add_car(car: Car, vehicle_service: VehicleService = Depends(VehicleService.get_service)) -> Car:
    response = vehicle_service.create_car(car)
    return response


@vehicle_router.get('/type/{vehicle_type}/')
async def get_all_vehicles_with_type(
    vehicle_type: TypeOfVehicle,
    vehicle_service: VehicleService = Depends(VehicleService)
) -> List[Union[Ship, AirCraft, Car]]:
    return vehicle_service.get_vehicles_with_current_type(vehicle_type)


@vehicle_router.get('/{vehicle_name}/')
async def get_vehicle_by_name(
    vehicle_name: str,
    vehicle_service: VehicleService = Depends(VehicleService.get_service)
) -> Union[Vehicle, str]:
    result = vehicle_service.get_vehicle_by_name(vehicle_name)
    return '-' if result is None else result


@engine_router.get('/')
async def get_engines(engine_service: EngineService = Depends(EngineService.get_service)) -> List[Engine]:
    response = engine_service.get_engines()
    return response


@engine_router.post('/')
async def add_engine(
    engine: Engine,
    engine_service: EngineService = Depends(EngineService.get_service)
) -> Engine:
    response = engine_service.add_engine(engine)
    return response
