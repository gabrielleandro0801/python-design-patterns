from typing import List

from builder.domain.builder import Builder
from builder.domain.car import Car, Engine, Body, Wheel


class Director:

    def __init__(self):
        self.__builder: Builder = None

    def set_builder(self, builder: Builder):
        self.__builder = builder

    def get_car(self) -> Car:
        car: Car = Car()

        body: Body = self.__builder.get_body()
        car.set_body(body)

        engine: Engine = self.__builder.get_engine()
        car.set_engine(engine)

        wheels: List[Wheel] = self.__builder.get_wheels()
        car.set_wheels(wheels)

        return car
