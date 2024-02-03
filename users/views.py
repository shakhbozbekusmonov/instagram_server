from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import SignUpSerializer


class SignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]
