from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile, ProfileFollow
from .serializers import RegistrationSerializer, ProfileListSerializer, ProfileDetailSerializer, \
    ProfileFollowSerializer


class RegistrationView(generics.GenericAPIView):
    """
    Регистрация пользователя.
    """
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "success": "User Created Successfully. Now perform Login to get your token"
        })


class ProfileListView(generics.ListAPIView):
    """
    Вывод всех пользователей без статей.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer


class ProfileDetailView(APIView):
    """
    Вывод пользователя с его статьями.
    """
    def get(self, request, id_profile):
        profile = Profile.objects.get(id=id_profile)
        serializer = ProfileDetailSerializer(profile)
        return Response(serializer.data)


class ProfileAddFollowView(generics.GenericAPIView):
    """
    Добавления подписки на пользователя.
    """
    serializer_class = ProfileFollowSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, id_follow_profile, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.initial_data['follow_profile'] = id_follow_profile
        serializer.initial_data['profile'] = self.request.user.id
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "Follow succeeded"})


class ProfileDestroyFollowView(APIView):
    """
    Удаления подписки на пользователя.
    """
    permission_classes = [IsAuthenticated]

    def delete(self, request, id_follow_profile, *args, **kwargs):
        id_profile = self.request.user.id
        instance = ProfileFollow.objects.get(profile=id_profile, follow_profile=id_follow_profile)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
