from typing import List

from builder.domain.car import Wheel, Engine, Body


class Builder:

    def get_wheels(self) -> List[Wheel]:
        pass

    def get_engine(self) -> Engine:
        pass

    def get_body(self) -> Body:
        pass
