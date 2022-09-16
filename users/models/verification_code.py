from django.db import models

class VerificationCodeQuerySet(models.QuerySet):
    pass

class VerificationCode(models.Model):
    phone = models.CharField(max_length=64)
    code = models.CharField(max_length=8)
    verifies_at = models.DateTimeField(null=True)
    expires_at = models.DateTimeField()

    objects = VerificationCodeQuerySet.as_manager()

    class Meta:
        db_table = "users_verification_codes"
