from abc import ABC
from enum import Enum
from typing import List
from random import randrange, uniform
from dataclasses import dataclass

from pydantic import BaseModel


class TypeOfVehicle(str, Enum):
    AIR = 'air'
    GROUND = 'ground'
    SEA = 'sea'


class Vehicle(ABC, BaseModel):
    name: str
    weight: float
    range_of_movement: float


class AirCraft(Vehicle):
    type_of_vehicle: TypeOfVehicle = TypeOfVehicle.AIR
    components: List[str]

    @staticmethod
    def generate_random_aircraft() -> 'AirCraft':
        return AirCraft(
            name=''.join([chr(randrange(97, 122)) for _ in range(0, randrange(8))]),
            weight=round(uniform(1_000, 123_000), 2),
            range_of_movement=round(uniform(2_000, 11_000), 2),
            components=['wings', 'tail', 'main_corpus']
        )


class Ship(Vehicle):
    type_of_vehicle: TypeOfVehicle = TypeOfVehicle.SEA
    waterline: float

    @staticmethod
    def generate_random_ship() -> 'Ship':
        return Ship(
            name=''.join([chr(randrange(97, 122)) for _ in range(0, randrange(8))]),
            weight=round(uniform(1_000, 123_000), 2),
            range_of_movement=round(uniform(2_000, 11_000), 2),
            waterline=randrange(30, 80)
        )


class Car(Vehicle):
    type_of_vehicle: TypeOfVehicle = TypeOfVehicle.GROUND
    aceleration: float

    @staticmethod
    def generate_random_car() -> 'Car':
        return Car(
            name=''.join([chr(randrange(97, 122)) for _ in range(0, randrange(8))]),
            weight=round(uniform(1_000, 123_000), 2),
            range_of_movement=round(uniform(2_000, 11_000), 2),
            aceleration=randrange(3, 20)
        )


@dataclass(frozen=True)
class Engine:
    energy: int
    capacity: float


def generate_random_vehicle() -> Vehicle:
    rand = randrange(1, 4)
    match rand:
        case 1:
            return AirCraft.generate_random_aircraft()
        case 2:
            return Ship.generate_random_ship()
        case 3:
            return Car.generate_random_car()


vehicle_db = [generate_random_vehicle() for _ in range(30)]


engine_db = [Engine(randrange(1, 100), round(uniform(1.0, 100.0), 2)) for _ in range(10)]


if __name__ == '__main__':
    for vehicle in vehicle_db:
        print(vehicle, '\n')