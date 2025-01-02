from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from .models import Tweet
from .serializers import RegisterSerializer, TweetSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class TweetListCreateView(ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]  # Allow unauthenticated users to view tweets
        return [IsAuthenticated()]  # Only authenticated users can create tweets

    def perform_create(self, serializer):
        # Associate the tweet with the current authenticated user
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            # Handle case where an unauthenticated user tries to post a tweet (optional)
            serializer.save()


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom JWT token view to include additional user data in the response.
    """
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        response.data['user_id'] = user.id
        response.data['username'] = user.username
        return response
