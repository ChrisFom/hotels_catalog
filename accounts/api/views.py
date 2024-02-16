from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout

from .serializers import UserRegisterSerializer, UserLoginSerializer, EmptySerializer
from accounts.models import CustomUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class AuthViewSet(viewsets.GenericViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny, ]
    serializer_class = EmptySerializer
    serializer_classes = {
        'register': UserRegisterSerializer,
        'login': UserLoginSerializer,
    }

    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            _ = CustomUser.objects.create_user(**serializer.validated_data)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response({'detail': 'User successfully authenticated.'},
                                status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid credentials.'},
                                status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'],)
    def logout(self, request):
        logout(request)
        return Response({'detail': 'User successfully logout.'})

    def get_serializer_class(self):

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()
