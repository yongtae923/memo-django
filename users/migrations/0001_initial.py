# Generated by Django 3.2 on 2022-09-23 01:14

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('nickname', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'users_accounts',
            },
        ),
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=8)),
                ('verifies_at', models.DateTimeField(null=True)),
                ('expires_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'users_verification_codes',
            },
        ),
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update_at', models.DateTimeField()),
                ('_password_key', models.CharField(max_length=512)),
                (
                    'account',
                    models.ForeignKey(
                        db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='users.account'
                    ),
                ),
            ],
            options={
                'db_table': 'users_credentials',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=512)),
                ('refresh_token', models.CharField(max_length=512)),
                ('expires_at', models.DateTimeField()),
                (
                    'account',
                    models.ForeignKey(
                        db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='users.account'
                    ),
                ),
            ],
            options={
                'db_table': 'users_access_tokens',
            },
        ),
    ]
