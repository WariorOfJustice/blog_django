from django.core.mail import send_mail

from profile_user.models import ProfileFollow


def send_mail_message(author, title_post, text_post):
    """
    Отправляем письмо по почте при создании поста, если пользователи подписаны на его автора.
    """
    head_message = f'Новый пост от {author}'
    message = f'{author} сделал следующий пост:\n\nЗаголовок:{title_post}\nТекст:{text_post}'
    emails_to_send = [i.profile.email for i in ProfileFollow.objects.filter(follow_profile_id=author.id)]
    send_mail(head_message, message, 'blog.fbv.2.1@gmail.com', emails_to_send)
