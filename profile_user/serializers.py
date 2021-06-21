from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueTogetherValidator

from article.serializers import ArticleSerializer
from profile_user.models import Profile, ProfileFollow


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Сериазизатор регистрации пользователя.
    Есть дополнительная валидация пароля.
    """
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    def create(self, validated_data):
        profile = Profile.objects.create_user(username=validated_data['username'],
                                              email=validated_data['email'],
                                              password=validated_data['password'],
                                              first_name=validated_data['first_name'],
                                              last_name=validated_data['last_name'])
        return profile

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs


class ProfileListSerializer(serializers.ModelSerializer):
    """
    Сериализатор вывода всех профилей без статей.
    """
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'img_profile']


class ProfileDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор вывода пользователя с его статьями.
    """
    article_set = ArticleSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'img_profile', 'article_set']


class ProfileFollowSerializer(serializers.ModelSerializer):
    """
    Сериализатор подписки пользователей друг на друга.
    """
    class Meta:
        model = ProfileFollow
        fields = '__all__'
        validators = [UniqueTogetherValidator(queryset=ProfileFollow.objects.all(),
                                              fields=['profile', 'follow_profile'])]
