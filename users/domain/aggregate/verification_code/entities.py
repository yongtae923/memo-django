from dataclasses import dataclass
from datetime import datetime, timedelta
from random import randrange
from typing import Optional, Text
import uuid
from pytz import UTC

@dataclass
class VerificationCodeEntity:
    phone: Text
    code: Text = str(randrange(1000000, 10000000))
    expires_at: datetime = datetime.now() + timedelta(minutes=5)
    verifies_at: Optional[datetime] = None
    context_key:Text = str(uuid.uuid4())
    id: Optional[int] = None

    def verify(self):
        if self.expires_at > datetime.now(UTC):
            """
            만료 됐지는ㄴ
            """
            raise Exception

        self.verifies_at = datetime.now()
