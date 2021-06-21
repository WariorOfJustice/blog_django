from rest_framework import serializers

from article.models import Article, Comment


class ArticleCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор создания статьи.
    """
    class Meta:
        model = Article
        fields = ('title', 'text', 'rubric', 'author')
        read_only_fields = ['author']


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор вывода комментария.
    """
    author = serializers.StringRelatedField()
    article = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id', 'author', 'article', 'updated', 'created']


class ArticleSerializer(serializers.ModelSerializer):
    """
    Сериализатор вывода статьи.
    """
    author = serializers.StringRelatedField()
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'text', 'created', 'updated', 'rubric', 'comment_set']
        read_only_fields = ['id', 'author', 'created', 'updated', 'comment_set']


class CreateCommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор создания комментария.
    """
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['text', 'article', 'author']
