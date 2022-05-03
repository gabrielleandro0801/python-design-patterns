from factory_method.creators.abstract_person_creator import PersonCreator
from factory_method.domain.abstract_person import Person
from factory_method.domain.product_pj import ProductPJ


class CreatorPJ(PersonCreator):
    def __init__(self):
        print("Creating class CreatorPJ")

    def instantiate_person(self) -> Person:
        print("Creating class ProductPJ")
        return ProductPJ()
