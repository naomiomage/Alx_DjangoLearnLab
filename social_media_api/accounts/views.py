# accounts/views.py
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import RegisterSerializer, LoginSerializer

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.get(user=user)
        return Response({'token': token.key, 'username': user.username}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data  # LoginSerializer returns the user object in validate()
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'username': user.username})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user = request.user
    data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'bio': getattr(user, 'bio', ''),
        'profile_picture': request.build_absolute_uri(user.profile_picture.url) if getattr(user, 'profile_picture') else None,
        'followers_count': user.followers.count(),
        'following_count': user.following.count(),
    }
    return Response(data)


# ---------- Follow / Unfollow endpoints ----------

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    target = get_object_or_404(User, pk=user_id)
    if target == request.user:
        return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
    request.user.follow(target)
    return Response({
        'detail': f'You are now following {target.username}.',
        'target_followers_count': target.followers.count()
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    target = get_object_or_404(User, pk=user_id)
    if target == request.user:
        return Response({'detail': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
    request.user.unfollow(target)
    return Response({
        'detail': f'You have unfollowed {target.username}.',
        'target_followers_count': target.followers.count()
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_following(request):
    qs = request.user.following.all()
    data = [{'id': u.id, 'username': u.username, 'followers_count': u.followers.count(), 'following_count': u.following.count()} for u in qs]
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_followers(request):
    qs = request.user.followers.all()
    data = [{'id': u.id, 'username': u.username, 'followers_count': u.followers.count(), 'following_count': u.following.count()} for u in qs]
    return Response(data)
