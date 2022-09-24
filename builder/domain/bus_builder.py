from typing import List

from builder.domain.builder import Builder
from builder.domain.car import Wheel, Body, Engine


class BusBuilder(Builder):
    def __init__(self):
        self.__wheels: List[Wheel] = []
        self.__engine: Engine = Engine()
        self.__body: Body = Body()

    def get_wheels(self) -> List[Wheel]:
        for _ in range(0, 6):
            wheel: Wheel = Wheel()
            wheel.size = 22
            self.__wheels.append(wheel)
        return self.__wheels

    def get_engine(self) -> Engine:
        self.__engine.horsepower = 750
        return self.__engine

    def get_body(self) -> Body:
        self.__body.shape = "Bus"
        return self.__body
