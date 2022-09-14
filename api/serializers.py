# api/serializers.py
from rest_framework import serializers

from .models import Account


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'name',
            'nickname',
            'phone',
            'email',
            'created_at',
        )
        read_only_fields = ('created_at',)
