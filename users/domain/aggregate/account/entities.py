from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Text


@dataclass
class AccessTokenEntity:
    token: Text
    refresh_token: Text
    expires_at: datetime


@dataclass
class CredentialEntity:
    provider: Text
    last_updated_at: datetime
    password: Text


@dataclass
class AccountEntity:
    name: Text
    nickname: Text
    phone: Text
    email: Text
    created_at: datetime = datetime.now()
    credentials: List[CredentialEntity] = List[CredentialEntity]
    access_tokens: List[AccessTokenEntity] = List[AccessTokenEntity]
    id: Optional[int] = None
