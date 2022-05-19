from typing import Any

from factory_method_specification.domain.abstract_validator import DocumentValidator


class CNPJValidator(DocumentValidator):
    def __init__(self, specification):
        self.__specification: Any = specification

    def validate(self, document: str) -> bool:
        pass