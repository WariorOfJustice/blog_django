from django import forms
from django.forms import TextInput, Textarea

from article.models import Article, Comment


class ArticleForm(forms.ModelForm):
    """
    Форма для добавления поста.
    """
    class Meta:
        model = Article
        fields = ('title', 'text', 'rubric', 'author')

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Заголовок статьи'
            }),
            'text': Textarea(attrs={
                'placeholder': 'Содержание поста'
            }),
            'rubric': TextInput(attrs={
                'placeholder': 'Тема поста'
            }),
        }


class ChangeArticleForm(forms.ModelForm):
    """
    Форма для изменения поста.
    """
    class Meta:
        model = Article
        fields = ('title', 'text', 'rubric', 'author')

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Заголовок статьи',
            }),
            'text': Textarea(attrs={
                'placeholder': 'Содержание поста'
            }),
            'rubric': TextInput(attrs={
                'placeholder': 'Тема поста'
            }),
        }


class CommentForm(forms.ModelForm):
    """
    Форма для создания комментария.
    """
    class Meta:
        model = Comment
        fields = ('text', 'article', 'author')

        widgets = {
            'text': Textarea(attrs={
                'placeholder': 'Текст комментария'
            })}
