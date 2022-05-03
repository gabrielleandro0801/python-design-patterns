from factory_method.domain.abstract_person import Person


class ProductPJ(Person):

    def do_post(self):
        print("Calling PJ endpoint...")
