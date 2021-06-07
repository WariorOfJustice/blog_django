from django.contrib.auth.models import User

from article.models import Article
from profile_user.models import Profile


def saving_and_registering_user(form):
    """
    Сохраняем User-а джанги по форме.
    + по данным от юзера создаем его профиль.
    """
    first_name = form.data['first_name']
    last_name = form.data['last_name']
    username = form.data['username']
    form.save()
    new_user = User.objects.get(username=username)
    Profile.objects.create(user=new_user, first_name=first_name, last_name=last_name)


def check_subscription_flag(current_user, user):
    """
    Проверка возможности подписки/отписки на(от) пользователя.
    """
    if current_user.id == user.id:
        return None
    elif str(user.id) not in current_user.subscriptions.split():
        return True
    else:
        return False


def add_subscriber(current_user, user_for_subscribe):
    """
    Добавляем подписку текущему пользователю и подписчика пользователю, на которого подписаны.
    """
    current_user.subscriptions = current_user.subscriptions + ' ' + str(user_for_subscribe.id)
    current_user.save()
    user_for_subscribe.profile.my_subscribers = user_for_subscribe.profile.my_subscribers + ' ' + str(current_user.id)
    user_for_subscribe.profile.save()


def delete_subscriber(current_user, user_for_delete_subscribe):
    """
    Удаляем подписку текущего пользователя и подписчика пользователя , на которого были подписаны.
    """
    # удалаяем подписку у текущего пользователя
    subscriptions_list = current_user.subscriptions.split()
    index_to_remove = subscriptions_list.index(str(user_for_delete_subscribe.id))
    del subscriptions_list[index_to_remove]
    current_user.subscriptions = ' '.join(subscriptions_list)
    current_user.save()
    # удаляем подписчика в виде текущего пользователя
    subscribers_list = user_for_delete_subscribe.profile.my_subscribers.split()
    index_2_to_remove = subscribers_list.index(str(current_user.id))
    del subscribers_list[index_2_to_remove]
    user_for_delete_subscribe.profile.my_subscribers = ' '.join(subscribers_list)
    user_for_delete_subscribe.profile.save()


def get_subscriptions_posts(user):
    """
    Получаем посты пользователей, на которых подписан текущий пользователь.
    """
    subscriptions_int_list = [int(i) for i in user.subscriptions.split()]
    articles_of_subscribe = Article.objects.filter(author_id__in=subscriptions_int_list)
    return articles_of_subscribe
