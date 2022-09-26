from typing import List, Text

from users.domain.aggregate.account.entities import AccessTokenEntity, AccountEntity
from users.domain.aggregate.account.repositories import AccountRepository
from users.domain.mappers import AccountMapper
from users.models import AccessToken, Account
from users.models.account import AccountQuerySet


class ORMAccountRepository(AccountRepository):
    def save(self, entity: AccountEntity) -> None:
        Account.objects.create(
            name=entity.name,
            nickname=entity.nickname,
            phone=entity.phone,
            email=entity.email,
        )

    def find_account_by_email(self, email: Text) -> List[AccountEntity]:
        accounts: AccountQuerySet = Account.objects.filter(email=email)
        return [AccountMapper.to_entity(account) for account in accounts]

    def find_account_by_phone(self, phone: Text) -> List[AccountEntity]:
        accounts: AccountQuerySet = Account.objects.filter(phone=phone)
        return [AccountMapper.to_entity(account) for account in accounts]

    def verify_password(self, account: AccountEntity, password: Text) -> bool:
        return account.credentials[0].password == password

    def save_access_token(self, account: AccessTokenEntity) -> None:
        AccessToken.objects.create(account=account)
