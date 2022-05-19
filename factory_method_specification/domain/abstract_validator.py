from abc import ABC, abstractmethod


class DocumentValidator(ABC):

    @abstractmethod
    def validate(self, document: str) -> bool:
        pass
