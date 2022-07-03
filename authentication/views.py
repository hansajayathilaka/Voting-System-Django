from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework import views, permissions, status, generics, viewsets
from rest_framework.response import Response

from authentication.serializers import LoginSerializer, UserSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        logout(self.request)
        login(self.request, user)
        return Response(UserSerializer(user).data, status=status.HTTP_202_ACCEPTED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        logout(self.request)
        return Response(None, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        # Your logic should be all here
        if self.request.method == 'POST':
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
        return super().get_permissions()

    def list(self, request, **kwargs):
        return super().list(request, **kwargs)

    def create(self, request, **kwargs):
        return super().create(request, **kwargs)

    def retrieve(self, request, pk=None, **kwargs):
        return super().retrieve(request, pk, **kwargs)

    def update(self, request, pk=None, **kwargs):
        return super().update(request, pk, **kwargs)

    def partial_update(self, request, pk=None, **kwargs):
        return super().partial_update(request, pk, **kwargs)

    def destroy(self, request, pk=None, **kwargs):
        return Response(None, status=status.HTTP_406_NOT_ACCEPTABLE)
