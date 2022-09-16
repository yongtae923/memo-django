from datetime import datetime
from typing import List

from users.application.dtos.auth import PhoneNumberRequestDTO, VerifyCodeDTO
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
    def __init__(self, verification_code_repository: VerificationCodeRepository):
        self.verification_code_repository = verification_code_repository

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


def provide_auth_service():
    verification_code_repository = provide_verification_code_repository()
    return AuthService(verification_code_repository=verification_code_repository)
