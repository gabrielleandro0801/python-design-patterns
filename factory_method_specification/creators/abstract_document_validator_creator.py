from abc import ABC, abstractmethod

from factory_method_specification.domain.abstract_validator import DocumentValidator


def default_person_type():
    raise Exception('Person Type not defined')


class DocumentValidatorCreator(ABC):

    @staticmethod
    def create(person_type: str) -> DocumentValidator:
        from factory_method_specification.creators.cpf_validator_creator import CPFValidatorCreator
        from factory_method_specification.creators.cnpj_validator_creator import CNPJValidatorCreator

        options: dict = {
            'F': lambda: CPFValidatorCreator(),
            'J': lambda: CNPJValidatorCreator()
        }

        creator: DocumentValidatorCreator = options.get(person_type, default_person_type)()
        return creator.instantiate_validator()

    @abstractmethod
    def instantiate_validator(self) -> DocumentValidator:
        pass
