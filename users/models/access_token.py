from django.db import models


class AccessToken(models.Model):
    token = models.CharField(max_length=512)
    refresh_token = models.CharField(max_length=512)
    expires_at = models.DateTimeField()
    account = models.ForeignKey('users.Account', db_constraint=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "users_access_tokens"
