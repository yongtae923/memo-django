from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response

from users.domain.aggregate.verification_code.entities import VerificationCodeEntity
from users.application.dtos.auth import PhoneNumberRequestDTO, VerifyCodeDTO
from users.application.services.auth import provide_auth_service


class AuthViewSet(viewsets.GenericViewSet):
    """
    api/users/auth/
    """
    def list(self,request):
        """
        GET
        :return:
        """
        pass

    def create(self,request):
        """
        POST
        :return:
        """
        pass

    def retrieve(self,request,sno):
        """
        GET {lookup}
        :return:
        """
        pass

    def update(self,request,sno):
        """
        PUT {lookup}
        :return:
        """
        pass

    def partial_update(self,request):
        """
        PATCH {lookup}
        :return:
        """
        pass

    def destroy(self):
        """
        DELETE {lookup}
        :return:
        """
        pass


    @action(detail=False)
    def codes(self,request):
        """
        /api/users/auth/codes/
        """
        dto = PhoneNumberRequestDTO(data=request.data)
        dto.is_valid(raise_exception=True)
        entity:VerificationCodeEntity =provide_auth_service().request_verification_code(dto)

        return Response(dict(code=entity.code),status=status.HTTP_200_OK)

    @action(detail=False,url_path='codes/verify')
    def codes_verify(self,request):
        dto = VerifyCodeDTO(data=request.data)
        dto.is_valid(raise_exception=True)
        provide_auth_service().verify_code(dto)

        return Response(status=status.HTTP_200_OK)

