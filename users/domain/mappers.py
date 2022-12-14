from typing import Any, Dict, Optional, Text

from dacite import from_dict

from users.domain.aggregate.account.entities import AccountEntity
from users.domain.aggregate.verification_code.entities import VerificationCodeEntity
from users.models import Account, VerificationCode


class VerificationCodeMapper:
    @staticmethod
    def to_entity(data: Dict[Text, Any] = None, *, from_obj: Optional[VerificationCode] = None):
        if from_obj:
            data = dict(
                id=from_obj.id,
                phone=from_obj.phone,
                code=from_obj.phone,
                verifies_at=from_obj.verifies_at,
                expires_at=from_obj.expires_at,
            )

        return from_dict(
            data_class=VerificationCodeEntity,
            data=data,
        )


class AccountMapper:
    @staticmethod
    def to_entity(data: Dict[Text, Any] = None, *, from_obj: Optional[Account] = None):
        if from_obj:
            data = dict(
                id=from_obj.id,
                name=from_obj.name,
                nickname=from_obj.nickname,
                phone=from_obj.phone,
                email=from_obj.email,
            )
        return from_dict(data_class=AccountEntity, data=data)
