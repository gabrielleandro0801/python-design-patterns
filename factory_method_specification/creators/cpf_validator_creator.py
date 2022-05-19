from factory_method_specification.creators.abstract_document_validator_creator import DocumentValidatorCreator
from factory_method_specification.domain.abstract_validator import DocumentValidator
from factory_method_specification.domain.cpf_validator import CPFValidator
from factory_method_specification.domain.specification.cpf import CPFRule


class CPFValidatorCreator(DocumentValidatorCreator):

    def instantiate_validator(self) -> DocumentValidator:
        return CPFValidator(CPFRule())
