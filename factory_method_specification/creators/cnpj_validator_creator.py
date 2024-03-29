from factory_method_specification.creators.abstract_document_validator_creator import DocumentValidatorCreator
from factory_method_specification.domain.abstract_validator import DocumentValidator
from factory_method_specification.domain.cnpj_validator import CNPJValidator
from factory_method_specification.domain.specification.cnpj import CNPJRule


class CNPJValidatorCreator(DocumentValidatorCreator):

    def instantiate_validator(self) -> DocumentValidator:
        return CNPJValidator(CNPJRule())
