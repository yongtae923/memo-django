from dataclasses import dataclass
from datetime import datetime, timedelta
from random import randrange
from typing import Optional, Text


@dataclass
class VerificationCodeEntity:
    phone: Text
    code: Text = str(randrange(1000000, 10000000))
    expires_at: datetime = datetime.now() + timedelta(minutes=5)
    verifies_at: Optional[datetime] = None
    id: Optional[int] = None
