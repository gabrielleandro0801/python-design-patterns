from typing import Any

from factory_method_specification.domain.abstract_validator import DocumentValidator


class CPFValidator(DocumentValidator):
    def __init__(self, specification):
        self.__specification: Any = specification

    def validate(self, document: str) -> bool:
        return self.__specification.is_satisfied_by(document)
