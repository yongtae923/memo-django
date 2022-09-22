from datetime import datetime, timedelta
from typing import List

from django.utils.crypto import get_random_string

from users.application.dtos.auth import LoginDTO, PhoneNumberRequestDTO, RegisterDTO, VerifyCodeDTO
from users.domain.aggregate.account.entities import AccessTokenEntity, AccountEntity
from users.domain.aggregate.account.repositories import AccountRepository, provide_account_repository
from users.domain.aggregate.verification_code.entities import VerificationCodeEntity
from users.domain.aggregate.verification_code.repositories import (
    VerificationCodeRepository,
    provide_verification_code_repository,
)


def generate_code():
    """
    public VerificationCode(string phone)
    {
        Id = Ulid.NewUlid().ToString();
        Phone = phone;
        Code = new Random().Next(100000, 1000000).ToString();
        VerifiesAt = null;
        ExpiresAt = DateTimeOffset.UtcNow.AddMinutes(5);
    }
    """


class AuthService:
    def __init__(self, verification_code_repository: VerificationCodeRepository, account_repository: AccountRepository):
        self.verification_code_repository = verification_code_repository
        self.account_repository = account_repository

    def request_verification_code(self, phone_number_request_dto: PhoneNumberRequestDTO) -> VerificationCodeEntity:
        """
        public async Task<StatusResponse> RequestVerificationCodeAsync(PhoneNumberRequestModel model)
        {
            // 전화번호가 올바른 형식인지 확인합니다.
            var phoneString = model.Phone;
            if (!PhoneNumberUtil.IsViablePhoneNumber(phoneString)) return new StatusResponse(StatusType.BadRequest);

            // 전화번호에 해당하는 인증코드를 생성하고 저장하고 반환합니다.
            var code = new VerificationCode(ParseToFormat(phoneString));

            _database.VerificationCodes.Add(code);
            await _database.SaveChangesAsync();

            return new StatusResponse(StatusType.Success, code.Code);
        }
        """

        phone_string = phone_number_request_dto.validated_data['phone']
        code_entity: VerificationCodeEntity = VerificationCodeEntity(phone=phone_string)
        self.verification_code_repository.save(code_entity)
        return code_entity

    def verify_code(self, dto: VerifyCodeDTO):
        """
         var matchedCodes = _database.VerificationCodes.Where(code =>
            code.Code == verifyingCode && code.Phone == ParseToFormat(phoneString));
        if (!matchedCodes.Any()) return new StatusResponse(StatusType.NotFound);
        """
        entity_list: List[VerificationCodeEntity] = self.verification_code_repository.find_codes_by_phone_and_code(
            code=dto.validated_data['code'], phone=dto.validated_data['phone']
        )
        if not entity_list:
            """
            인즈
            """
            raise Exception

        if any([entity.expires_at > datetime.now() for entity in entity_list]):
            """
            만ㄹ
            """
            raise Exception

    def register(self, dto: RegisterDTO):
        """

        // 만료되지 않고 활성화 되어있는 인증코드를 찾습니다.
        var validCodes = _database.VerificationCodes.Where(code =>
            code.Phone == parsedPhone && code.VerifiesAt < DateTimeOffset.UtcNow &&
            code.ExpiresAt > DateTimeOffset.UtcNow).ToList();
        if (validCodes.Count == 0) return new StatusResponse(StatusType.Forbidden);

        // 모든 활성 인증코드를 만료시킵니다.
        validCodes.ForEach(code => code.ExpiresAt = DateTimeOffset.UtcNow);

        // 계정과 엑세스토큰을 생성하고 반환합니다.
        var account = model.ToAccount(parsedPhone);
        var accessToken = new AccessToken(account);

        account.AccessTokens.Add(accessToken);
        account.Credentials.Add(new Credential(account, model.Password));
        _database.Accounts.Add(account);
        await _database.SaveChangesAsync();

        // 엑세스토큰을 반환합니다.
        return new StatusResponse(StatusType.Success, new AccessTokenResponse(accessToken));
        """
        valid_codes = self.verification_code_repository.find_active_codes(phone=dto.validated_data['phone'])
        if not valid_codes:
            raise Exception

        self.verification_code_repository.expire_active_codes(phone=dto.validated_data['phone'])

        account_entity: AccountEntity = AccountEntity(
            name=dto.name, nickname=dto.nickname, phone=dto.phone, email=dto.email
        )

        self.account_repository.save(account_entity)

    def login(self, dto: LoginDTO):
        if self.is_email(dto.id):
            account = self.account_repository.find_account_by_email(email=dto.id)
        elif self.is_phone(dto.id):
            account = self.account_repository.find_account_by_phone(phone=dto.id)
        else:
            raise Exception

        if account is None:
            raise Exception

        if not self.account_repository.verify_password(account, dto.password):
            raise Exception

        access_token_entity: AccessTokenEntity = AccessTokenEntity(
            token=get_random_string(), refresh_token=get_random_string(), expires_at=datetime.now() + timedelta(days=7)
        )

        self.account_repository.save_access_token(access_token_entity)

    def is_email(self, text: str) -> bool:
        # 이메일인지 확인
        pass

    def is_phone(self, text: str) -> bool:
        # 전화번호인지 확인
        pass


def provide_auth_service():
    verification_code_repository = provide_verification_code_repository()
    account_repository = provide_account_repository()
    return AuthService(verification_code_repository=verification_code_repository, account_repository=account_repository)
