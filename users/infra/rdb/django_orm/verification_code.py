from datetime import datetime
from typing import List, Text
from dataclasses import asdict

from users.domain.aggregate.verification_code.entities import VerificationCodeEntity
from users.domain.aggregate.verification_code.repositories import VerificationCodeRepository
from users.domain.mappers import VerificationCodeMapper
from users.models import VerificationCode
from users.models.verification_code import VerificationCodeQuerySet


class ORMVerificationCodeRepository(VerificationCodeRepository):
    def save(self, entity: VerificationCodeEntity) -> None:
        VerificationCode.objects.create(
            phone=entity.phone, code=entity.code, verifies_at=entity.verifies_at, expires_at=entity.expires_at
        )

    def find_codes_by_phone_and_code(self, code: Text, context_key: Text) -> VerificationCodeEntity:
        code_obj: VerificationCode = VerificationCode.objects.get(context_key=context_key, verifies_at__isnull=True, use_at__isnull=True)
        return VerificationCodeMapper.to_entity(from_obj=code_obj)


    def find_active_codes(self, context_key: Text)->List[VerificationCodeEntity]:
        code_obj: VerificationCode = VerificationCode.objects.get(
            context_key=context_key, verifies_at__isnull=False
        )
        return VerificationCodeMapper.to_entity(code_obj)

    def expire_active_codes(self, phone: Text):
        code_objs: VerificationCodeQuerySet = VerificationCode.objects.filter(phone=phone)
        code_objs.update(expires_at=datetime.now())
        return [VerificationCodeMapper.to_entity(code_obj) for code_obj in code_objs]

    def bulk_update(self,entity_list:List[VerificationCodeEntity],fields:tuple):
        objs =[VerificationCode(**asdict(entity)) for entity in entity_list]
        VerificationCode.objects.bulk_update(objs,fields)
