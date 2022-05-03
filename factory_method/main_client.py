from factory_method.creators.abstract_person_creator import PersonCreator
from factory_method.domain.abstract_person import Person

if __name__ == '__main__':
    person_type: str = 'F'
    product: Person = PersonCreator.create(person_type)

    product.do_post()
