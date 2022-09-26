from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.application.dtos.auth import LoginDTO, PhoneNumberRequestDTO, RegisterDTO, VerifyCodeDTO
from users.application.services.auth import provide_auth_service
from users.domain.aggregate.verification_code.entities import VerificationCodeEntity


class AuthViewSet(viewsets.GenericViewSet):
    """
    api/users/auth/
    """

    @action(detail=False)
    def codes(self, request):
        """
        /api/users/auth/codes/
        """
        dto = PhoneNumberRequestDTO(data=request.data)
        dto.is_valid(raise_exception=True)
        entity: VerificationCodeEntity = provide_auth_service().request_verification_code(dto)

        return Response(dict(code=entity.code, context_key=entity.context_key), status=status.HTTP_200_OK)

    @action(detail=False, url_path='codes/verify')
    def codes_verify(self, request):
        dto = VerifyCodeDTO(data=request.data)
        dto.is_valid(raise_exception=True)
        provide_auth_service().verify_code(dto)

        return Response(status=status.HTTP_200_OK)

    @action(detail=False, url_path='register')
    def register(self, request):
        dto = RegisterDTO(data=request.data)
        dto.is_valid(raise_exception=True)
        access_token: bytes = provide_auth_service().register(dto)

        return Response(data=access_token, status=status.HTTP_200_OK)

    @action(detail=False, url_path='login')
    def login(self, request):
        dto = LoginDTO(data=request.data)
        dto.is_valid(raise_exception=True)
        provide_auth_service().login(dto)

        return Response(status=status.HTTP_200_OK)
