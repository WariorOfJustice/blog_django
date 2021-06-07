from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from article.models import Article
from profile_user.forms import UserRegistrationForm
from profile_user.models import Profile
from profile_user.services import check_subscription_flag, add_subscriber, delete_subscriber, get_subscriptions_posts, \
    saving_and_registering_user


def registration_view(request):
    """
    Регистрация пользователя.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            saving_and_registering_user(form)
            return redirect('login')
        else:
            form = UserRegistrationForm(request.POST)
    else:
        form = UserRegistrationForm()
    return render(request, 'profile_user/registration_form.html', {'form': form})


def user_page_view(request, username):
    """
    Выводит страницу конкретного пользователя с его постами.
    + если пользователь авторизован, дает возможность подписаться/отписаться.
    """
    user = get_object_or_404(User, username=username)
    posts = Article.objects.filter(author_id__exact=user.id)
    referer_page = request.headers['Referer']
    # ошибка обрабатывает случай, когда current_user - это неавторизованный пользователь.
    try:
        subscription_flag = check_subscription_flag(request.user.profile, user)
    except AttributeError:
        subscription_flag = None
    return render(request, 'profile_user/user_posts.html', context={
        'selected_user': user, 'posts': posts, 'referer_page': referer_page, 'subscription_flag': subscription_flag})


def get_all_users_view(request):
    """
    Выводим список всех пользователей.
    """
    users = Profile.objects.all()
    return render(request, 'profile_user/all_users.html', {'users': users})


def add_subscriber_view(request, username):
    """
    Добавляем подписку текущему пользователю и подписчика пользователю, на которого подписаны.
    """
    add_subscriber(request.user.profile, User.objects.get(username=username))
    return redirect('user_page', username)


def delete_subscriber_view(request, username):
    """
    Удаляем подписку текущего пользователя и подписчика пользователя , на которого были подписаны.
    """
    delete_subscriber(request.user.profile, User.objects.get(username=username))
    return redirect('user_page', username)


def get_subscriptions_posts_view(request, user_id):
    """
    Выводим посты пользователей, на которых подписан текущий пользователь.
    """
    articles_of_subscribe = get_subscriptions_posts(Profile.objects.get(id=user_id))
    return render(request, 'profile_user/subscriptions.html', {'context': articles_of_subscribe})
