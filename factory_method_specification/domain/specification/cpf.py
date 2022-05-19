from simple_specification import Specification


class CPFRule(Specification):

    def is_satisfied_by(self, document: str) -> bool:
        condition = (
                MustBeAValidSequenceRule() &
                RestOfDivisionMustBeEqualsToPenultimateNumberRule() &
                RestOfDivisionMustBeEqualsToLastNumberRule()
        )
        return condition.is_satisfied_by(document)


# https://texasvaluesaction.org/victor-o-silva/simple-specification/blob/master/tests.py

class MustBeAValidSequenceRule(Specification):

    def is_satisfied_by(self, document: str) -> bool:
        # Obtém os números do CPF e ignora outros caracteres
        cpf = [int(char) for char in document if char.isdigit()]

        # Verifica se o CPF tem 11 caracteres
        if len(cpf) != 11:
            return False

        # Verifica se o CPF tem todos os números iguais, ex: 11111111111
        return False if cpf == cpf[::-1] else True


class RestOfDivisionMustBeEqualsToPenultimateNumberRule(Specification):

    def is_satisfied_by(self, document: str) -> bool:
        # Obtém os números do CPF e ignora outros caracteres
        cpf = [int(char) for char in document if char.isdigit()]

        # Obtém o penúltimo dígito do CPF
        penultimate_number = cpf[9]

        # Obtém o dígito verificador
        value = sum((cpf[num] * (10 - num) for num in range(0, 9)))
        digit = ((value * 10) % 11) % 10

        # Verifica se o dígito verificador passado é igual ao encontrado pela fórmula
        return False if digit != penultimate_number else True


class RestOfDivisionMustBeEqualsToLastNumberRule(Specification):

    def is_satisfied_by(self, document: str) -> bool:
        # Obtém os números do CPF e ignora outros caracteres
        cpf = [int(char) for char in document if char.isdigit()]

        # Obtém o último dígito do CPF
        last_digit = cpf[10]

        # Obtém o dígito verificador
        value = sum((cpf[num] * (11 - num) for num in range(0, 10)))
        digit = ((value * 10) % 11) % 10

        # Verifica se o dígito verificador passado é igual ao encontrado pela fórmula
        return False if digit != last_digit else True
