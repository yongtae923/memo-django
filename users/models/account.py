from django.db import models


# Create your models here.
class AccountQuerySet(models.QuerySet):
    pass


class Account(models.Model):
    name = models.CharField(max_length=128)
    nickname = models.CharField(max_length=256)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=256)
    objects = AccountQuerySet.as_manager()

    class Meta:
        db_table = "users_accounts"
