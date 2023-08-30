from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    
class UserLogin(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        if email is None:
            return Response({'error': 'Email not informed'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = User.objects.get(email=email)
            if not user.check_password(request.data['password']):
                return Response({'error': 'Email or password incorrect'}, status=status.HTTP_400_BAD_REQUEST)
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_403_FORBIDDEN)