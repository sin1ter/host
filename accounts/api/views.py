from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema

from .serializers import LoginSerializer, RegisterSerializer

class LoginView(APIView):
    permission_classes = []  # No restriction for login
    
    @extend_schema(
        summary="Login user with username or email and password",
        request=LoginSerializer,
        responses={200: 'Access and refresh tokens'}
    )

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

class RegisterView(APIView):
    permission_classes = []  # No restriction for registration

    @extend_schema(
        summary="Register a new user with username, email, and password",
        request=RegisterSerializer,
        responses={201: 'User registered with access and refresh tokens'}
    )

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)