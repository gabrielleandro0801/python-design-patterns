from factory_method.creators.abstract_person_creator import PersonCreator
from factory_method.domain.abstract_person import Person
from factory_method.domain.product_pf import ProductPF


class CreatorPF(PersonCreator):
    def __init__(self):
        print("Creating class CreatorPF")

    def instantiate_person(self) -> Person:
        print("Creating class ProductPF")
        return ProductPF()
