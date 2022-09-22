from abc import ABC

from users.domain.aggregate.account.entities import AccessTokenEntity, AccountEntity


class AccountRepository(ABC):
    def save(self, entity: AccountEntity) -> None:
        pass

    def find_account_by_email(self, email: str) -> AccountEntity:
        pass

    def find_account_by_phone(self, phone: str) -> AccountEntity:
        pass

    def verify_password(self, account: AccountEntity, password: str) -> bool:
        pass

    def save_access_token(self, token: AccessTokenEntity):
        pass


def provide_account_repository():
    from users.infra.rdb.django_orm.account import ORMAccountRepository

    return ORMAccountRepository()
