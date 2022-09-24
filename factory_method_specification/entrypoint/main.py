from factory_method_specification.creators.abstract_document_validator_creator import DocumentValidatorCreator
from factory_method_specification.domain.abstract_validator import DocumentValidator

if __name__ == '__main__':
    # CPF
    person_type: str = 'F'
    document: str = "00000000000"

    document_validator: DocumentValidator = DocumentValidatorCreator.create(person_type)
    is_valid = document_validator.validate(document)

    definition = "is" if is_valid else "is not"
    print(f"CPF [{document}] {definition} valid")

    # CPF
    person_type = 'J'
    document: str = "0000000000191"

    document_validator: DocumentValidator = DocumentValidatorCreator.create(person_type)
    is_valid = document_validator.validate(document)

    definition = "is" if is_valid else "is not"
    print(f"CNPJ [{document}] {definition} valid")
