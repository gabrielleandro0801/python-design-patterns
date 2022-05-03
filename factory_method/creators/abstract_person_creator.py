from abc import ABC, abstractmethod

from factory_method.domain.abstract_person import Person


def default_person_type():
    raise Exception('Person Type not defined')


class PersonCreator(ABC):

    @staticmethod
    def create(person_type: str) -> Person:
        from factory_method.creators.creator_pf import CreatorPF
        from factory_method.creators.creator_pj import CreatorPJ

        options: dict = {
            'F': lambda: CreatorPF(),
            'J': lambda: CreatorPJ()
        }

        creator: PersonCreator = options.get(person_type, default_person_type)()
        return creator.instantiate_person()

    @abstractmethod
    def instantiate_person(self) -> Person:
        pass
