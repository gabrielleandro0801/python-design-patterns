from itertools import cycle

from simple_specification import Specification


class CNPJRule(Specification):

    def is_satisfied_by(self, document: str) -> bool:
        condition = (
                MustBeAValidSequenceRule() &
                ValidatorsDigitRule()
        )
        return condition.is_satisfied_by(document)


class MustBeAValidSequenceRule(Specification):

    def is_satisfied_by(self, document: str) -> bool:
        # Obtém os números do CPF e ignora outros caracteres
        if len(document) != 14:
            return False

        # Verifica se o CNPJ tem todos os números iguais, ex: 11111111111111
        if document in (c * 14 for c in "1234567890"):
            return False

        return True


class ValidatorsDigitRule(Specification):

    def is_satisfied_by(self, document: str) -> bool:
        cnpj_reverse = document[::-1]

        for i in range(2, 0, -1):
            cnpj_enum = zip(cycle(range(2, 10)), cnpj_reverse[i:])
            dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
            if cnpj_reverse[i - 1:i] != str(dv % 10):
                return False

        return True
