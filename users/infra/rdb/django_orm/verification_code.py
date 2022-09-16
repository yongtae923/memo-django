from typing import Text,List

from users.domain.aggregate.verification_code.entities import VerificationCodeEntity
from users.domain.aggregate.verification_code.repositories import VerificationCodeRepository
from users.domain.mappers import VerificationCodeMapper
from users.models import VerificationCode
from users.models.verification_code import VerificationCodeQuerySet


class ORMVerificationCodeRepository(VerificationCodeRepository):
    def save(self,entity:VerificationCodeEntity) ->None:
        VerificationCode.objects.create(phone=entity.phone,code=entity.code,verifies_at=entity.verifies_at,expires_at=entity.expires_at)

    def find_codes_by_phone_and_code(self,phone:Text,code:Text) ->List[VerificationCodeEntity]:
        code_objs:VerificationCodeQuerySet= VerificationCode.objects.filter(phone=phone,code=code)
        return [VerificationCodeMapper.to_entity(code_obj) for code_obj in code_objs]

