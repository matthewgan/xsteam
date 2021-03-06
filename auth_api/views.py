from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework import status, views
from rest_framework.response import Response

from .serializers import UserSerializer


class LoginView(views.APIView):
    @method_decorator(csrf_protect)
    def post(self, request):
        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password")
        )

        if user is None or not user.is_active:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username or password incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response(UserSerializer(user).data)


class LogoutView(views.APIView):
    @staticmethod
    def get(request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
