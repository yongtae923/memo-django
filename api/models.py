from django.db import models


class Account(models.Model):
    name = models.CharField(verbose_name='이름', max_length=255)
    nickname = models.CharField(verbose_name='닉네임', max_length=255)
    phone = models.CharField(verbose_name='전화번호', max_length=255)
    email = models.CharField(verbose_name='이메일', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
