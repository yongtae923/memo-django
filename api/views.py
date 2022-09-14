# api/views.py
from rest_framework import permissions, viewsets

from .models import Account
from .serializers import PostSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()
