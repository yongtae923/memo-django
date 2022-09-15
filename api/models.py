from django.db import models


class AccessToken(models.Model):
    token = models.CharField(verbose_name='엑세스 토큰', max_length=255)
    refresh_token = models.CharField(verbose_name='리프레시 토큰', max_length=255)
    expires_at = models.DateTimeField(verbose_name='만료일시')

    def __str__(self):
        return self.token


class Credential(models.Model):
    password_key = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.provider


class Account(models.Model):
    name = models.CharField(verbose_name='이름', max_length=255)
    nickname = models.CharField(verbose_name='닉네임', max_length=255)
    phone = models.CharField(verbose_name='전화번호', max_length=255)
    email = models.CharField(verbose_name='이메일', max_length=255)
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)

    access_token = models.ForeignKey(AccessToken, on_delete=models.CASCADE, null=True)
    credential = models.ForeignKey(Credential, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class VerificationCode(models.Model):
    name = models.CharField(verbose_name='이름', max_length=255)
    phone = models.CharField(verbose_name='전화번호', max_length=255)
    code = models.CharField(verbose_name='이메일', max_length=255)
    verifies_at = models.DateTimeField(verbose_name='인증일시')
    expires_at = models.DateTimeField(verbose_name='만료일시')

    def __str__(self):
        return self.name
