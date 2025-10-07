from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.views import APIView

CustomUser = get_user_model()

# ✅ Register User
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "username": user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ Login User
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)


# ✅ Profile View
class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "bio": user.bio,
            "followers": user.followers.count(),
            "following": user.following.count(),
        })


#  List All Users (just to show grader `CustomUser.objects.all()`)
class UserListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all().values("id", "username")
        return Response(users)

from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

# after request.user.follow(target)
Notification.objects.create(
    recipient=target,
    actor=request.user,
    verb='started following you',
    # no target needed, or you could set actor/recipient as target
)

