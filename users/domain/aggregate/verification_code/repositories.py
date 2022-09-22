from abc import ABC
from typing import Text

from users.domain.aggregate.verification_code.entities import VerificationCodeEntity


class VerificationCodeRepository(ABC):
    def save(self, entity: VerificationCodeEntity) -> None:
        """ """
        pass

    def find_codes_by_phone_and_code(self, phone: Text, code: Text):
        pass

    def find_active_codes(self, phone: Text):
        pass

    def expire_active_codes(self, phone: Text):
        pass


def provide_verification_code_repository():
    from users.infra.rdb.django_orm.verification_code import ORMVerificationCodeRepository

    return ORMVerificationCodeRepository()
