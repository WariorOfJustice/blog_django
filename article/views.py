from django.shortcuts import render, redirect, get_object_or_404

from article.forms import ArticleForm, CommentForm, ChangeArticleForm
from article.models import Article, Comment
from profile_user.models import Profile
from article.services import send_mail_message, change_form_parameters, redirect_after_delete, change_article


def get_main_page_view(request):
    """
    Выводит главную страницу со всеми постами.
    """
    return render(request, 'article/main_page.html', context={'context': Article.objects.all()})


def create_post_view(request):
    """
    Форма для создания нового поста.
    """
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        user = Profile.objects.get(id=request.user.pk)
        change_form_parameters(form, user)
        if form.is_valid():
            form.save()
            send_mail_message(form.data['author'], form.data['title'], form.data['text'])
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'article/add_post.html', {'form': form})


def article_page_view(request, article_id):
    """
    Выводит страницу поста.
    """
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article_id__exact=article_id)
    referer_page = request.headers['Referer']
    return render(request, 'article/article_page.html',
                  context={'article': article, 'comments': comments, 'referer_page': referer_page})


def add_comment_view(request, article_id):
    """
    Форма для добавления комментария.
    """
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article_id__exact=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        user = Profile.objects.get(id=request.user.pk)
        change_form_parameters(form, user, article)
        if form.is_valid():
            form.save()
            return redirect('article_page', article_id)
    else:
        form = CommentForm()
    return render(request, 'article/add_comment.html',
                  {'form': form, 'article': article, 'comments': comments})


def delete_post_view(request, post_id):
    """
    Удаляет пост.
    Флаг нужен, чтобы не редиректить на удаленный пост.
    """
    Article.objects.get(id=post_id).delete()
    referer_page = request.headers['Referer']
    flag_for_determining_redirect = redirect_after_delete(referer_page)
    if flag_for_determining_redirect is False:
        return redirect('home')
    else:
        return redirect(referer_page)


def change_post_view(request, post_id):
    """
    Форма для изменения поста.
    Саму форму мы не сохраняем, а используем данные из нее для изменения атрибутов поста.
    """
    post = Article.objects.get(id=post_id)
    if request.method == 'POST':
        form = ChangeArticleForm(request.POST)
        user = Profile.objects.get(id=request.user.pk)
        change_form_parameters(form, user)
        if form.is_valid():
            change_article(post, form)
            return redirect('article_page', post_id)
    else:
        form = ChangeArticleForm(initial={'title': post.title, 'text': post.text, 'rubric': post.rubric})
    return render(request, 'article/change_post.html', {'form': form, 'post_id': post_id})
