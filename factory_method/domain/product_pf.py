from factory_method.domain.abstract_person import Person


class ProductPF(Person):

    def do_post(self):
        print("Calling PF endpoint...")
