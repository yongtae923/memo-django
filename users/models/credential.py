from django.db import models


class Credential(models.Model):
    class ProviderChoice(models.TextChoices):
        google = "google"
        twitter = "twitter"

    last_update_at = models.DateTimeField()
    _password_key = models.CharField(max_length=512)
    account = models.ForeignKey('users.Account', db_constraint=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "users_credentials"
