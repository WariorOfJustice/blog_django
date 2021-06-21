from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from profile_user.models import ProfileFollow
from .models import Article, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import ArticleCreateSerializer, ArticleSerializer, CreateCommentSerializer
from .services import send_mail_message


class ListArticleView(generics.ListAPIView):
    """
    Вывод всех статей.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CreateArticleView(generics.CreateAPIView):
    """
    Создание статьи + отправка сообщения об этом подписчикам.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        send_mail_message(self.request.user, serializer.data['title'], serializer.data['text'])


class DetailArticleView(generics.RetrieveUpdateDestroyAPIView):
    """
    Вывод одной статьи.
    Если ты ее автор, то + возможность обновлять, удалять.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CreateCommentView(generics.CreateAPIView):
    """
    Создание комментария.
    """
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ListFollowsArticlesView(generics.ListAPIView):
    """
    Вывод статей пользователей, на которых подписан.
    """
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        profile_id = self.request.user.id
        follows_authors = [i.follow_profile.id for i in ProfileFollow.objects.filter(profile_id=profile_id)]
        return Article.objects.filter(author_id__in=follows_authors)
